import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config(object):
    SQLALCHEMY_DATABASE_URI=os.getenv('dbstring')
    SQLALCHEMY_DATABASE_URI=os.getenv('proddb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('secret_key') or 'pewpewpeng'
