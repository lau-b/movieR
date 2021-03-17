import os

class Config(object):
    SQLALCHEMY_DATABASE_URI='postgres://laurin@localhost:5432/movier'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
