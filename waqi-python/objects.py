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
    # def __init__(self, data):
    #     self.pm2_5 = data[]
    #     self.pm10 = data[]
    #     self.no2 = data[]
    #     self.co = data[]
    #     self.so2 = data[]
    #     self.ozone = data[]
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
        self.attributions = [Attribution(attrib)
                             for attrib in data['attributions']]
        self.dominantpol = data['dominentpol']
        # self.iaqi = Iaqi(data['iaqi'])


class Time():
    def __init__(self, data):
        self.time = data['s']
        self.tz = data['tz']
        self.datetime = convert_to_datetime(self.time, self.tz)
