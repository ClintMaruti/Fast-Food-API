import os
from configparser import ConfigParser


class Config():
    """Base config class"""
    DEBUG = False
   
class Testing(Config):
    """Configuration for testing environment"""
    DEBUG = True

class Development(Config):
    """Configuration for testing environment"""
    DEBUG = True


class Production(Config):
    """Configuration for production environment"""
    DEBUG = False


app_config = {
    'testing': Testing,
    'production': Production,
    'development': Development,
}
