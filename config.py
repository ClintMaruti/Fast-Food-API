import os
from configparser import ConfigParser


class Config():
    """Base config class"""
    DEBUG = False
    
    JWT_SECRET_KEY = os.getenv('SECRET_KEY')
   
class Development(Config):
    """Configuration for development environment"""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class Testing(Config):
    """Configuration for testing environment"""
    DEBUG = True
    TESTING = True

class Production(Config):
    """Configuration for production environment"""
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}