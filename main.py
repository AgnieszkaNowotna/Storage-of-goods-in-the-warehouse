from flask import Flask, render_template, redirect, url_for,flash
from models import product
from forms import ProductForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

@app.route("/")
def homepage():
    return render_template('base.html')

@app.route("/product_list")
def product_list():
    product_list = product.load_products()
    form = ProductForm()
    return render_template('product_list.html', product_list = product_list, form = form)

@app.route("/product_list/add", methods = ['POST'])
def add_product():
    form = ProductForm()
    error = ""
    if form.validate_on_submit():
        product.add_product(form.data)
        product.save_list()
    flash('New product has been added')
    return redirect(url_for('product_list'))

if __name__=="__main__":
    app.run(debug=True)