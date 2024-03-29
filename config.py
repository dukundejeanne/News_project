import os
class Config:
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/sources?apiKey=18b06483376c497f815f4bea6845a114'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=18b06483376c497f815f4bea6845a114'
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')

    @staticmethod
    def init_app(app):
        pass
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}


