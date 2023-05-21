import json

from flask import Blueprint, request, jsonify
from database.DatabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

seller_api = Blueprint('seller_api', __name__)


@seller_api.route('/seller', methods=['POST'])
def create_seller():
    try:
        seller_data = request.get_json()

        result = create_single_row('Sellers', seller_data)

        if result:
            username = seller_data.get('SellerName')
            return jsonify({'message': f'Seller {username} created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create seller'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating seller', 'error': str(e)}), 500


@seller_api.route('/seller/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = get_single_row('Sellers', 'SellerID', seller_id)
    if seller:
        seller_json_str = seller[0]
        seller_dict = json.loads(seller_json_str)
        return jsonify(seller_dict), 200
    else:
        return jsonify({'message': 'Seller not found'}), 404


@seller_api.route('/sellers', methods=['GET'])
def get_sellers():
    sellers = get_multiple_rows('Sellers', 'SellerID')
    if sellers:
        return jsonify({'sellers': sellers}), 200
    else:
        return jsonify({'message': 'No sellers found'}), 404


@seller_api.route('/seller/<int:seller_id>', methods=['PUT'])
def update_seller(seller_id):
    try:
        seller_data = request.get_json()

        result = delete_or_update_row('Sellers', seller_id, 'SellerID', _Action.UPDATE, seller_data)

        return jsonify({'seller_id': seller_id, 'success': result, 'message': 'Seller updated successfully' if result else 'Failed to update seller'}), 200
    except Exception as e:
        return jsonify({'message': 'Error updating seller', 'error': str(e)}), 500


@seller_api.route('/seller/<int:seller_id>', methods=['DELETE'])
def delete_seller(seller_id):
    result = delete_or_update_row('Sellers', seller_id, 'SellerID', _Action.DELETE)

    if result:
        return jsonify({'message': f'Seller with id = {seller_id} deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete seller'}), 500
