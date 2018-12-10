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
        if r.status_code != 200:
            raise ApiError('GET {} {}'.format(url, r.status_code))
        if r.json()['status'] == 'ok':
            return r.json()['data']
        elif r.json()['status'] == 'error':
            raise ApiError('GET {} {}: {}'.format(
                url, r.json()['status']), r.json()['message'])
        else:
            return None


    def get_station_by_path(self, path):
        url = _FEED_PATH_URL.format(path)
        data = self._get(url)
        if data is not None:
            return Station(data)
        else:
            return None


    def get_station_by_id(self, uid):
        url = _FEED_ID_URL.format(uid)
        data = self._get(url)
        if data is not None:
            return Station(data)
        else:
            return None


    def get_local_station(self):
        url = _FEED_LOCAL_URL
        data = self._get(url)
        if data is not None:
            return Station(data)
        else:
            return None


    def get_station_by_latlng(self, lat, lng):
        url = _FEED_GEO_URL.format(lat, lng)
        data = self._get(url)
        if data is not None:
            return Station(data)
        else:
            return None


    def list_stations_by_bbox(self, lat1, lng1, lat2, lng2, detailed=False):
        bbox = [min(lat1, lat2), min(lng1, lng2), max(lat1, lat2),
                max(lng1, lng2)]
        latlng = (',').join(list(map(str, bbox)))
        url = _MAP_BBOX_URL.format(latlng)
        data = self._get(url)
        if data is not None:
            stations_locs = [Location(station) for station in data]
            if detailed:
                return [self.get_station_by_id(loc.uid)
                        for loc in stations_locs]
            else:
                return stations_locs
        else:
            return None


    def list_stations_by_keyword(self, keyword, detailed=False):
        url = _SEARCH_URL.format(keyword)
        data = self._get(url)
        if data is not None:
            stations = [(result['uid'],result['station']['name'])
                        for result in data]
            if detailed:
                return [self.get_station_by_id(station[0])
                        for station in stations]
            else:
                return stations
        else:
            return None
 