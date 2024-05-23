"""
This module configures the SQLAlchemy database URI based on the environment.
If the Flask environment is set to 'testing', it uses an in-memory SQLite database,
otherwise, it retrieves the SQLAlchemy database URI from the environment variables.
"""
import os
from dotenv import load_dotenv
"""Module for configuration settings.
- loads environment variables using dotenv
- sets up various configuration parameters for the Flask app.
"""



SECRET_KEY = "390ccbf61aa82533c12e8c6c1d2eb1dc"


SQLALCHEMY_DATABASE_URI ='sqlite:///carts.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False

