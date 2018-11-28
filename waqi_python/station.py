from datetime import datetime as dt
from dateutil.parser import parse


class Attribution():
    def __init__(self, data):
        self.name = data['name']
        self.url = data['url']


class Location():
    def __init__(self, data):
        self.uid = data['uid']
        self.lat = data['lat']
        self.lon = data['lon']
        self.aqi = data['aqi']


class Station():
    def __init__(self, data):
        self.idx = data['idx']
        self.aqi = data['aqi']

        try:
            time = data['time']['s']
            tz = data['time']['tz']
            self.time = parse(f'{time} {tz}')
        except ValueError:
            self.time = None

        self.name = data['city']['name']
        self.geo = data['city']['geo']
        self.url = data['city']['url']

        attributions = []
        for attrib in data['attributions']:
            attributions.append(Attribution(attrib))
        self.attributions = attributions

        self.raw = data
