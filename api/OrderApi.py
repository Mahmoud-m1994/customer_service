import os

import requests
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify
from database.DatabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

load_dotenv()
order_api = Blueprint('orders_api', __name__)


@order_api.route('/orders', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()

        result = create_single_row('Orders', order_data)

        if result:
            order_id = order_data.get('OrderID')

            products = order_data.get('products', [])

            for product_data in products:
                base_url = os.getenv('API_URL')
                response = requests.post(f'{base_url}/orders/{order_id}/products', json=product_data)

                if response.status_code != 200:
                    return jsonify({'message': 'Failed to add products to order'}), 500

            return jsonify({'message': f'Order {order_id} created successfully and products added'}), 200
        else:
            return jsonify({'message': 'Failed to create order'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating order', 'error': str(e)}), 500


@order_api.route('/orders/<int:order_id>/products', methods=['POST'])
def add_product_to_order(order_id):
    try:
        # Get the JSON data from the request
        product_data = request.get_json()

        # Call the create_single_row function to add the product to the order
        result = create_single_row('OrderProducts', {
            'OrderID': order_id,
            'ProductID': product_data['ProductID'],
            'Quantity': product_data['Quantity']
        })

        if result:
            return jsonify({'message': f'Product added to order {order_id} successfully'}), 200
        else:
            return jsonify({'message': 'Failed to add product to order'}), 500
    except Exception as e:
        return jsonify({'message': 'Error adding product to order', 'error': str(e)}), 500


@order_api.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = get_single_row('Orders','OrderID', order_id)
    if order:
        order_dict = {column: value for column, value in order.items()}
        return jsonify(order_dict), 200
    else:
        return jsonify({'message': 'Order not found'}), 404


@order_api.route('/orders', methods=['GET'])
def get_orders():
    orders = get_multiple_rows('Orders', 'OrderID')
    if orders:
        orders_list = [order for order in orders]
        return jsonify({'orders': orders_list}), 200
    else:
        return jsonify({'message': 'No orders found'}), 404


@order_api.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        # Get the JSON data from the request
        order_data = request.get_json()

        # Call the delete_or_update_row function to update the order
        result = delete_or_update_row('Orders', order_id, 'OrderID', _Action.UPDATE, order_data)

        return jsonify({'order_id': order_id, 'success': result, 'message': 'Order updated successfully' if result else 'Failed to update order'}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating order', 'error': str(e)}), 500


@order_api.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    result = delete_or_update_row('Orders', order_id, 'OrderID', _Action.DELETE)

    if result:
        return jsonify({'message': f'Order with id = {order_id} deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete order'}), 500
