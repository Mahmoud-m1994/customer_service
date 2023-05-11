import json

from flask import Blueprint, request, jsonify
from database.DtabaseManager import get_single_row, get_multiple_rows, create_single_row, delete_or_update_row, _Action

seller_api = Blueprint('seller_api', __name__)


@seller_api.route('/seller', methods=['POST'])
def create_seller():
    try:
        # Get the JSON data from the request
        seller_data = request.get_json()

        # Call the create_single_row function to create a new seller
        result = create_single_row('Sellers', seller_data)

        if result:
            username = seller_data.get('seller_name')
            return jsonify({'message': f'Seller {username} created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create seller'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating seller', 'error': str(e)}), 500


@seller_api.route('/seller/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = get_single_row('Sellers', seller_id)
    if seller:
        seller_json_str = seller[0]
        seller_dict = json.loads(seller_json_str)
        return jsonify(seller_dict), 200
    else:
        return jsonify({'message': 'Seller not found'}), 404


@seller_api.route('/sellers', methods=['GET'])
def get_sellers():
    sql_query = f"SELECT * FROM Sellers"
    sellers = get_multiple_rows(sql_query)
    if sellers:
        return jsonify({'sellers': sellers}), 200
    else:
        return jsonify({'message': 'No sellers found'}), 404


@seller_api.route('/seller/<int:seller_id>', methods=['DELETE'])
def delete_seller(seller_id):
    result = delete_or_update_row('Sellers', seller_id, _Action.DELETE)

    if result:
        return jsonify({'message': 'Seller deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete seller'}), 500
