import json

from flask import Blueprint, request, jsonify
from database.DatabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

product_api = Blueprint('product_api', __name__)


@product_api.route('/product', methods=['POST'])
def create_product():
    try:
        # Get the JSON data from the request
        product_data = request.get_json()

        # Call the create_single_row function to create a new product
        result = create_single_row('Product1', product_data)

        if result:
            username = product_data.get('ProductName')
            return jsonify({'message': f'product {username} created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create product'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating product', 'error': str(e)}), 500


@product_api.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_single_row('Product1', 'ProductID', product_id)
    if product:
        product_json_str = product[0]
        product_dict = json.loads(product_json_str)
        return jsonify(product_dict), 200
    else:
        return jsonify({'message': 'product not found'}), 404


@product_api.route('/products', methods=['GET'])
def get_products():
    products = get_multiple_rows('Product1', 'ProductID')
    if products:
        return jsonify({'products': products}), 200
    else:
        return jsonify({'message': 'No products found'}), 404


@product_api.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        # Get the JSON data from the request
        product_data = request.get_json()

        # Call the delete_or_update_row function to update the product
        result = delete_or_update_row('Product1', product_id, 'ProductID', _Action.UPDATE, product_data)

        return jsonify({'product_id': product_id, 'success': result, 'message': 'product updated successfully' if result else 'Failed to update product'}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating product', 'error': str(e)}), 500


@product_api.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    result = delete_or_update_row('Product1', product_id, 'ProductID', _Action.DELETE)

    if result:
        return jsonify({'message': f'product with id = {product_id} deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete product'}), 500
