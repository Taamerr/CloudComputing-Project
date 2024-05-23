"""Module for configuration settings.
- loads environment variables using dotenv
- sets up various configuration parameters for the Flask app.
"""



SECRET_KEY = "390ccbf61aa82533c12e8c6c1d2eb1dc"


SQLALCHEMY_DATABASE_URI ='sqlite:///users.db'

SQLALCHEMY_TRACK_MODIFICATIONS = False
