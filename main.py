from flask import Flask, render_template, redirect, url_for, flash, request
from forms import ProductForm
import models

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

ITEMS = models.load_values()

@app.route("/")
def homepage():
    return render_template('base.html')

@app.route("/product_list")
def product_list():
    form = ProductForm()
    return render_template('product_list.html', product_list = ITEMS, form = form)

@app.route("/product_list/add", methods = ['POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        data = form.data
        models.add_product(data)
        models.save_list()
    return redirect(url_for('product_list'))

@app.route('/sell/<product>', methods = ['GET', 'POST'])
def sell_product(product):
    item = ITEMS[product]
    unit = item.unit
    if request.method == "POST":
        amount = int(request.form.get("quantity"))
        models.sell_product(item, amount)
        models.save_list()
        flash(f'{amount}{unit} of {product} has been sold')
        return redirect(url_for('product_list'))
    return render_template('sell_form.html', item = item)

if __name__=="__main__":
    app.run(debug=True)