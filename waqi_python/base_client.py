import os

class BaseClient():
    def __init__(self):
        self.params = {'token': os.environ['AQIPY_TOKEN']}
        self.base_url = 'http://api.waqi.info/'