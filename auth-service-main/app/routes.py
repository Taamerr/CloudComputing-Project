"""
Routes for User Registration, Login, and Password Reset

This module defines the routes for user registration, login, and password reset
functionality, providing RESTful endpoints for managing user accounts and
password recovery.

Endpoints:
- /api/register: Register a new user.
- /api/login: Log in a user.
- /api/reset-password: Initiate a password reset, verify reset tokens, and reset passwords.

Returns: JSON responses with appropriate status codes.
"""

from flask import request, jsonify
from werkzeug.security import generate_password_hash
from app import app, db
from app.services import register_user, login_user
from app.models import PasswordResetToken, User

@app.route('/api/status', methods=['GET'])
def health():
    """Check the health status of the application."""
    return jsonify({"message": "application is healthy"}), 200

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    print("username")
    print(username)
    response, status_code = register_user(username, email, password)
    return jsonify(response), status_code

@app.route('/api/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    response, status_code = login_user(identifier, password)
    return jsonify(response), status_code


