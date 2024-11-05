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

@app.route('/upd_prod', methods=['POST', 'GET'])
def upd_product():
    if request.method == "POST":
        prod_id = int(request.form['id'])
        title = request.form.get('title')
        description = request.form.get('description')
        done = request.form.get('done')

        # Busca el producto en la lista de productos y actualízalo
        for product in products:
            if product['id'] == prod_id:
                product['title'] = title
                product['description'] = description
                product['done'] = done
                break

        return redirect(url_for('upd_product'))
    
    return render_template('update_prod.html', title='Editar Producto', products=products)


@app.route('/del_prod', methods=['POST', 'GET'])
def del_product():
    if request.method == "POST":
        prod_id = int(request.form['id'])

        # Busca el producto en la lista de productos y actualízalo
        for product in products:
            if product['id'] == prod_id:
                product.delete(prod_id)
                break

        return redirect(url_for('upd_product'))
    
    return render_template('delete_prod.html', title='Editar Producto', products=products)

    
if __name__ == '__main__':
    app.run(debug=True, port=4000)
