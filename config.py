import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    MAIL_USE_TLS = True

    FLASK_ENV = os.environ.get('FLASK_ENV')

    # SQLAlchemy configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @staticmethod
    def init_app(app):
        if os.environ.get('FLASK_ENV') is None:
            raise KeyError('FLASK_ENV variable not set')
        if os.environ.get('DATABASE_URL') is None:
            raise KeyError('DATABASE_URL variable not set')


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class QAConfig(Config):
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class ProductionConfig(Config):
    SSL_DISABLE = (os.environ.get('SSL_DISABLE') or 'True') == 'True'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'qa': QAConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
