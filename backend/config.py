import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Config for database connection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # API Key for Etherscan
    ETHERSCAN_API_KEY = os.environ.get('ETHERSCAN_API_KEY')
    ETHERSCAN_API_ENDPOINT = "https://api.etherscan.io/api"
