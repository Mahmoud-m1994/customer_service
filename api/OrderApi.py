import json
from flask import Blueprint, request, jsonify
from database.DatabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

order_api = Blueprint('orders_api', __name__)


@order_api.route('/order', methods=['POST'])
def create_order():
    try:
        # Get the JSON data from the request
        order_data = request.get_json()

        # Call the create_single_row function to create a new order
        result = create_single_row('Orders', order_data)

        if result:
            order_id = order_data.get('OrderID')
            return jsonify({'message': f'Order {order_id} created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create order'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating order', 'error': str(e)}), 500


@order_api.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = get_single_row('Orders', order_id)
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
