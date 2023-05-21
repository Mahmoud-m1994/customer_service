from flask import Flask
from api.SellerApi import seller_api
from api.ProductApi import product_api
from api.OrderApi import order_api
from api.IssueApi import issues_api

app = Flask(__name__)

app.register_blueprint(seller_api)
app.register_blueprint(product_api)
app.register_blueprint(order_api)
app.register_blueprint(issues_api)

if __name__ == '__main__':
    print("Hei from customer service")
    app.run()