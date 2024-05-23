"""
This module contains Flask routes for managing a shopping cart.

Endpoints:
- GET '/': Retrieve all items in the cart.
- GET '/<int:item_id>': Retrieve a specific item in the cart by its ID.
- POST '/add': Add a new item to the cart.
- PUT '/<int:item_id>': Update an item in the cart.
- DELETE '/<int:item_id>': Delete an item from the cart.
"""
from flask import jsonify, request
from app import app
from app.services.cart_service import (
    add_item_to_cart,
    get_cart_items,
    get_cart_item_by_id,
    update_cart_item,
    delete_cart_item,
)

class CartError(Exception):
    """Custom exception for cart operations."""
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

@app.route('/cart', methods=['GET'])
def get_cart():
    """Route to retrieve all items in the cart."""
    try:
        cart_items = get_cart_items()
        return jsonify({'cart_items': cart_items}), 200
    except CartError as e:
        return jsonify({'error': str(e)}), e.status_code



@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Route to add a new item to the cart."""
    try:
        data = request.get_json()
        product_name = data.get('product_name')
        quantity = data.get('quantity')
        price = data.get('price')

        if not all([product_name, quantity, price]):
            return jsonify({'error': 'Missing data'}), 400

        new_item = add_item_to_cart(product_name, quantity, price)
        return jsonify({'message': 'Item added to cart successfully', 'item': new_item}), 201
    except CartError as e:
        return jsonify({'error': str(e)}), e.status_code
