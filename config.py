import os


class Config():
    """Base config class"""
    DEBUG = False


class Development(Config):
    """Configuration for development environment"""


class Testing(Config):
    """Configuration for testing environment"""
    DEBUG = True


class Production(Config):
    """Configuration for production environment"""
    DEBUG = False


app_config = {
    'development': Development,
    'testing': Testing,
    'production': Production
}