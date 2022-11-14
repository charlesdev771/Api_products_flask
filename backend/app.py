from flask import Flask, jsonify, request
app = Flask(__name__)

products = [
    {
        'id': 1,
        'título': 'Sabao',
        'autor': 'sei la'
    },
    {
        'id': 2,
        'título': 'livro',
        'autor': 'jooj'
    },
    {
        'id': 3,
        'título': 'filme legal',
        'autor': 'charles'
    },
]
@app.route('/products',methods=['POST'])
def include_new_product():
    new_product = request.get_json()
    products.append(new_product)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


@app.route('/product/<int:id>', methods=['GET'])
def get_products_by_id(id):
    for product in products:
        if product.get('id') == id:
            return jsonify(product)
        

@app.route('/products/<int:id>', methods=['PUT'])
def edit_product_by_id(id):
    product_alter = request.get_json()
    for indice, product in enumerate(products):
        if product.get('id') == id:
            products[indice].update(product_alter)
            return jsonify(products[indice])   
        
@app.route('/products/<int:id>',methods=['DELETE'])
def delete_product(id):
    for indice, product in enumerate(products):
        if product.get('id') == id:
            del products[indice]

    return jsonify(products) 


app.run(debug=True)