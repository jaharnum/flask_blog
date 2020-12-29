import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    
    #  Flask and extensions use the value of the secret key to generate signatures / tokens
    #  that ensure the host server can be correctly identified and protected from attack
    # TODO best practice is to set key in server env and remove hardcoded temp key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'TEMP_KEY'

    #  SQLALCHEMY
    #  Defaults to root dir if DATABASE_URL is not set
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  #  Do not signal the app when db is modified
    
