from flask import Flask, request, jsonify
from database.DtabaseManager import create_single_row

app = Flask(__name__)


@app.route('/seller', methods=['POST'])
def create_seller():
    try:
        # Get the JSON data from the request
        seller_data = request.get_json()

        # Call the create_single_row function to create a new seller
        result = create_single_row('Seller', seller_data)

        if result:
            username = seller_data.get('seller_name')
            return jsonify({'message': f'Seller {username} created successfully'}), 200
        else:
            return jsonify({'message': 'Failed to create seller'}), 500
    except Exception as e:
        return jsonify({'message': 'Error creating seller', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
