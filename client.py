import requests
import os


TOKEN = os.environ['AQIPY_TOKEN']


def _url(path):
    return 'http://api.waqi.info/' + path


def get_city_feed(city):
    r = requests.get(_url(f'feed/{city}/?token={TOKEN}'))
    return r.json()


def get_local_feed():
    r = requests.get(_url(f'feed/here/?token={TOKEN}'))
    return r.json()


def get_feed_by_location(lat, lng):
    r = requests.get(_url(f'/feed/geo:{lat};{lng}/?token={TOKEN}'))
    return r.json()


# TODO(danoscarmike): what is the best format to pass a bounding box?
# Is there a standard?
def list_stations_in_bounds(lat1, lng1, lat2, lng2, raw=False):
    latlng = (',').join(list(map(str, [lat1, lng1, lat2, lng2])))
    r = requests.get(_url(f'/map/bounds/?token={TOKEN}&latlng={latlng}'))
    return r.json()


def search_stations(keyword):
    r = requests.get(_url(f'search/?keyword={keyword}&token={TOKEN}'))
    return r.json()
