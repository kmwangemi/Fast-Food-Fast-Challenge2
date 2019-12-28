from flask import request, jsonify, make_response, Blueprint
from app.api.v1.models.order_model import Order

order = Blueprint('order', __name__, url_prefix='/api/v1')

#orders routes
@order.route('/orders',methods=['POST'])
def create_order():
    """Creates a new order"""
    try:
        data = request.get_json()
        if not data:
            return make_response(jsonify({
                "error" : "no order data input",
                'message' : 'Please make a new order'
                }), 404)
        title = data["title"],
        quantity = data["quantity"]
        description = data["description"]
    except Exception:
        return make_response(jsonify({
            "error" : "invalid order data input",
            "message" : "missing either title, quantity or description"
            }), 400)
    new_order = Order(title, quantity, description)
    new_order.add_orders()
    return make_response(jsonify({
        "status" : "OK",
        "Message" : "Order made successfully"
    }), 201)