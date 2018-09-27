import os
from configparser import ConfigParser


class Config():
    """Base config class"""
    DEBUG = False
    POSTGRES_DATABASE_URI = os.getenv('DATABASE_URL')
   
 
 
    def config(self, filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
 
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
            else:
                raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
        return db


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