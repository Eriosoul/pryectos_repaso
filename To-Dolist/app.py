# link de documentación: https://flask.palletsprojects.com/en/3.0.x/quickstart/


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

from products import products
from main import new_prod

@app.route('/product')
def product():
    return "Producto"

@app.route('/post_product', methods=['GET'])
def the_products():
    return f'{products}'

@app.route('/new_prod', methods=['POST', 'GET'])
def new_products():
    new_prod
    return new_prod

if __name__ == '__main__':
    app.run(debug=True, port=4000)
