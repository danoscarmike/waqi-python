import os
import requests


from .objects import *

_BASE_URL = 'http://api.waqi.info/'
_FEED_PATH_URL = _BASE_URL + 'feed/{}/'
_FEED_ID_URL = _BASE_URL + 'feed/@{}/'
_FEED_LOCAL_URL = _BASE_URL + 'feed/here/'
_FEED_GEO_URL = _BASE_URL + 'feed/geo:{};{}/'
_MAP_BBOX_URL = _BASE_URL + 'map/bounds/?latlng={}'
_SEARCH_URL = _BASE_URL + 'search/?keyword={}'

_PARAMS = {'token':os.environ['AQIPY_TOKEN']}

class WaqiClient():
    '''
    TODO: write the stuff
    '''

    def _get(self, url):
        r = requests.get(url, params=_PARAMS)
        if r.json()['status'] == 'ok':
            return r.json()['data']
        elif r.json()['status'] == 'error':
            print("Seriously, I need to figure out error handling.")
        else:
            return None
            print("Seriously, I need to figure out error handling.")


    def get_station_by_path(self, path):
        url = _FEED_PATH_URL.format(path)
        r = self._get(url)
        if r:
            return Station(r)
        else:
            return None
            print("I need to figure out error handling.")


    def get_station_by_id(self, uid):
        url = _FEED_ID_URL.format(uid)
        r = self._get(url)
        if r:
            return Station(r)
        else:
            return None
            print("I need to figure out error handling.")


    def get_local_station(self):
        url = _FEED_LOCAL_URL
        r = self._get(url)
        if r:
            return Station(r)
        else:
            return None
            print("I need to figure out error handling.")


    def get_station_by_latlng(self, lat, lng):
        url = _FEED_GEO_URL.format(lat, lng)
        r = self._get(url)
        if r:
            return Station(r)
        else:
            return None
            print("I need to figure out error handling.")


    def list_stations_by_bbox(self, lat1, lng1, lat2, lng2, complete=False):
        bbox = [min(lat1, lat2), min(lng1, lng2), max(lat1, lat2),
                max(lng1, lng2)]
        latlng = (',').join(list(map(str, bbox)))
        url = _MAP_BBOX_URL.format(latlng)
        r = self._get(url)
        if r:
            stations_locs = [Location(station) for station in r]
            if complete:
                return [self.get_station_by_id(loc.uid)
                        for loc in stations_locs]
            else:
                return stations_locs
        else:
            return None
            print("I need to figure out error handling.")


    def list_stations_by_keyword(self, keyword, complete=False):
        url = _SEARCH_URL.format(keyword)
        r = self._get(url)
        if r:
            stations = [(result['uid'],result['station']['name'])
                        for result in r]
            if complete:
                return [self.get_station_by_id(station[0])
                        for station in stations]
            else:
                return stations
        else:
            return None
            print("I need to figure out error handling.")
