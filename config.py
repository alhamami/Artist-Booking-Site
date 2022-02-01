import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
DATABASE_URI = 'postgres://gtuqhqanoxufnl:815acb66b2d4c39cde71934d5baf046f7561daa1c506767461019b89feb25e58@ec2-54-208-139-247.compute-1.amazonaws.com:5432/d9l02jj9k6snb6'
# Remove console warning
SQLALCHEMY_TRACK_MODIFICATIONS = False
