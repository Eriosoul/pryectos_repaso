# link de documentación: https://flask.palletsprojects.com/en/3.0.x/quickstart/


from flask import Flask

app = Flask(__name__)

from products import products

@app.route('/product')
def product():
    return "Producto"

if __name__ == '__main__':
    app.run(debug=True, port=4000)
