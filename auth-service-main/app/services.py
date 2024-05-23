"""
User Authentication and Password Reset Services Module
This module handles user registration, login functionality, including password hashing,
JWT token generation, and password reset services.
"""
from datetime import datetime, timedelta
import secrets
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
from app import app, db
from app.models import User, PasswordResetToken

'''def generate_tokens(user):
    """
     Generate access and refresh tokens for a user
     and store the refresh token in the database.
    """
    access_token = jwt.encode(
        {'username': user.username},
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    refresh_token = jwt.encode(
        {'username': user.username},
        app.config['REFRESH_SECRET_KEY'],
        algorithm='HS256'
    )

    user.refresh_token = refresh_token
    db.session.commit()

    return access_token, refresh_token'''

def register_user(username, email, password):
    """Register a new user and store their information in the database."""
    existing_user = User.query.filter_by(username=username).first() or \
                    User.query.filter_by(email=email).first()
    if existing_user:
        return {"message": "Username or email already exists"}, 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()



    return {
        "message": "Registration successful", 
    }, 201

def login_user(identifier, password):
    """Log in a user and return an access token upon successful login."""
    user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()

    if not user:
        return {"message": "User not found"}, 404

    if check_password_hash(user.password, password):

        return {
            "message": "Login successful",

        }, 200
    return {"message": "Invalid password"}, 401



