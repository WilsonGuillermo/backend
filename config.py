#### `config.py`:

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://majo:WilsonMemo_1964@localhost/boutique'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
