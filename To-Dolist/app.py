# link de documentación: https://flask.palletsprojects.com/en/3.0.x/quickstart/


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

from products import products
from backend_prod import MiProducts

m: MiProducts = MiProducts()
@app.route('/product')
def product():
    return render_template('table_prod.html', title='Bootstrap Table', products=products)
    # return products

@app.route('/new_prod', methods=['POST', 'GET'])
def new_products():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        done = request.form['done']
        nuevo_id = products[-1]['id'] + 1 if products else 1
        nuevo_prod = {
            'id': nuevo_id,
            'title': title,
            'description': description,
            'done': done
        }
        products.append(nuevo_prod)
        return redirect(url_for('product'))
    return render_template('add_prod.html', title='Add new Product')

    
if __name__ == '__main__':
    app.run(debug=True, port=4000)
