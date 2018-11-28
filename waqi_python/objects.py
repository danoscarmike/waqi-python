from .helpers import *


class Attribution():
    def __init__(self, data):
        self.name = data['name']
        self.url = data['url']


class City():
    def __init__(self, data):
        self.name = data['name']
        self.geo = data['geo']
        self.url = data['url']
        self.lat = self.geo[0]
        self.lon = self.geo[1]


class Iaqi():
    pass


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
        self.time = Time(data['time'])
        self.city = City(data['city'])

        attributions = []
        for attrib in data['attributions']:
            attributions.append(Attribution(attrib))
        self.attributions = attributions

        self.dominantpol = data['dominentpol']

        # self.iaqi = Iaqi(data['iaqi'])


class Time():
    def __init__(self, data):
        self.time = data['s']
        self.tz = data['tz']
        self.datetime = convert_to_datetime(self.time, self.tz)
