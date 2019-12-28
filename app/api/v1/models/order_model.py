'''Order Model'''
from datetime import datetime        

orders = []

class Order(object):
    """order model to store all orders data"""
    def __init__(self, title, quantity, description):
        self.title = title
        self.quantity = quantity
        self.description = description
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_orders(self):
        """Adds new orders to the orders list"""
        new_order = {
            'orderId' : str(len(orders)+1),
            'quantity' : self.quantity,
            'description' : self.description,
            'created_at' : self.now
        }
        orders.append(new_order)
        return new_order