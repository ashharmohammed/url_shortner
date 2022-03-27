from decouple import config

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = config('SECRET_KEY', default='sample_key')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
