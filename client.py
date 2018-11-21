import requests
import os


TOKEN = os.environ['AQIPY_TOKEN']


def _url(path):
    return 'http://api.waqi.info/' + path


def get_city_feed(city):
    return requests.get(_url(f'feed/{city}/?token={TOKEN}'))


def get_local_feed():
    return requests.get(_url(f'feed/here/?token={TOKEN}'))


def get_feed_by_location(lat, lng):
    return requests.get(_url(f'/feed/geo:{lat};{lng}/?token={TOKEN}'))

# TODO(danoscarmike): what is the best format to pass a bounding box? Is there a standard?
def list_stations_in_bounds(lat1, lng1, lat2, lng2, raw=False):
    latlng = (',').join(list(map(str, [lat1, lng1, lat2, lng2])))
    r = requests.get(_url(f'/map/bounds/?token={TOKEN}&latlng={latlng}'))

# TODO(danoscarmike): create a class for the response format??
    if not raw:
        for station in r.json()['data']:
            station_id = str(station['uid'])
            city_name = get_city_feed('@'+station_id).json()['data']['city']['name']
            print(city_name)
    else:
        print(r.json())


def search_stations(keyword):
    return requests.get(_url(f'search/?keyword={keyword}&token={TOKEN}'))
