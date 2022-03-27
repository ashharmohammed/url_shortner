from decouple import config


DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = config('SECRET_KEY', default='sample_key')
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
