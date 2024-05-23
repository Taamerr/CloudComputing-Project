"""Initialize Flask app with SQLAlchemy and Flask-Migrate.

Creates a Flask app instance, configures it using 'config.py',
sets up SQLAlchemy for database operations, and configures Flask-Migrate.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

"""Product database model."""

from datetime import datetime


class Product(db.Model):
    """Product class representing items in the database."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    dimension = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)


    def __repr__(self):
        """Representation of Product object."""
        return f"<product:{self.id}, name:'{self.name}'>"

with app.app_context():
    db.create_all()
@app.route('/product-create', methods=['POST'])
def create_product():
    """
    Creates a new product.

    Receives JSON data with product information: name, description, category, price.
    """
    try:
        data = request.get_json()
        new_product = Product(
            id=123,
            name=data["name"],
            description=data["description"],
            category=data["category"],
            weight=data["weight"],
            dimension=data["dimension"],
            price=data["price"]
        )
        db.session.add(new_product)
        print("addedd1")
        db.session.commit()
        print("addedd2")
        return jsonify({"message": "product added successfully"}), 201
    except KeyError as e:
        return f"missing field: {e}", 400
    except Exception as e:
        db.session.rollback()
        return str(e), 500

@app.route('/products', methods=['GET'])
def get_products():
    """
    Retrieves all products available in the database.
    """
    try:
        products = Product.query.all()
        formatted_products = [{
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "category": product.category,
            "weight": product.weight,
            "dimension": product.dimension,
            "price": product.price,

        } for product in products]

        if formatted_products:
            return jsonify(formatted_products), 200
        return jsonify({"message": "No products found"}), 404

    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieves a specific product by its ID.
    """
    try:
        product = db.session.get(Product, product_id)
        if product:
            product_dict = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "category": product.category,
                "weight": product.weight,
                "dimension": product.dimension,
                "price": product.price,
                "date_added": product.date_added.strftime("%Y-%m-%d %H:%M:%S")
            }
            return jsonify(product_dict), 200
        return jsonify({"message": "No product found"}), 404
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/products/<int:product_id>/update', methods=['PUT'])
def product_update(product_id):
    """
    Updates a specific product by its ID.

    Receives JSON data with updated product information: name, description, category, price.
    """
    try:
        product = db.session.get(Product, product_id)
        if product:
            data = request.get_json()
            product.name = data["name"]
            product.description = data["description"]
            product.weight=data["weight"],
            product.dimension=data["dimension"],
            product.category = data["category"]
            product.price = data["price"]

            db.session.commit()
            return jsonify({"message": "Product updated successfully"})
        return jsonify({"message" : "Invalid product url"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

@app.route('/products/<int:product_id>/delete', methods=['DELETE'])
def product_remove(product_id):
    """
    Deletes a specific product by its ID.
    """
    try:
        product = db.session.get(Product, product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted successfully"})
        return jsonify({"message" : "Invalid product"}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})

