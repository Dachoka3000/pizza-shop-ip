import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daisy:4H@ppyfeet@localhost/pizza'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
