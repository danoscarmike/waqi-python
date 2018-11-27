from datetime import datetime as dt


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

        time = data['time']['s']
        tz = data['time']['tz'].replace(':','')
        self.time = dt.strptime(f'{time} {tz}', '%Y-%m-%d %H:%M:%S %z')

        self.name = data['city']['name']
        self.geo = data['city']['geo']
        self.url = data['city']['url']

        attributions = []
        for attrib in data['attributions']:
            attributions.append(Attribution(attrib))
        self.attributions = attributions

        self.raw = data
