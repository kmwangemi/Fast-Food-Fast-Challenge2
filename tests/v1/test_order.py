"""The order endpoints test"""
from unittest import TestCase
import json
from instance.config import app_config
from app import create_app
from app.api.v1.views.order_view import Order


class OrderTestCase(TestCase):
    """The base class for order tests and tearing down"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.headers = {"content-type": "application/json"}
        self.no_json_headers = {}
        self.order = {
            "title" : "Chips and Ketchup",
            "quantity" : 2,
            "description" : "dry fried"
        }
        self.empty_order = {
            "title" : "",
            "quantity" : 0,
            "description" : ""
        }

    def test_order_created_successfully(self):
        """Test API can create an order successfully (POST request)"""
        res = self.client().post('/api/v1/orders', data=json.dumps(self.order), headers = self.headers)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Order made successfully', str(res.data))
    
    def test_order_cannot_create_with_invalid_details(self):
        """Tests that an order cannot be created with empty fields"""
        res = self.client().post('/api/v1/orders', data=json.dumps(self.empty_order), headers = self.headers)
        self.assertEqual(res.status_code, 201)


    def tearDown(self):
        pass