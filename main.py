from flask import Flask, render_template, redirect, url_for
from models import product
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('base.html')

@app.route("/product_list")
def product_list():
    product_list = product.load_products()
    return render_template('product_list.html', product_list = product_list)

if __name__=="__main__":
    app.run(debug=True)