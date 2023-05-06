from flask import Flask
from api.SellerApi import seller_api

app = Flask(__name__)

# Register the seller_api Blueprint
app.register_blueprint(seller_api)

# Other routes and configurations

if __name__ == '__main__':
    app.run()
