import requests

from .base_client import BaseClient
from .station import *


class WaqiClient(BaseClient):
    def _url(self, path):
        return self.base_url + path

    def get_station_by_city_name(self, city):
        r = requests.get(self._url(f'feed/{city}/'), params=self.params)
        # return r, r.json()
        if r.json()['status'] == 'ok':
            return Station(r.json()['data'])
        elif r.json()['status'] == 'error':
            return (r.json()['status'], r.json()['message'])
        else:
            return 'Unknown Error'

    def get_local_station(self):
        r = requests.get(self._url(f'feed/here/'), params=self.params)
        if r.json()['status'] == 'ok':
            return Station(r.json()['data'])
        elif r.json()['status'] == 'error':
            return (r.json()['status'], r.json()['message'])
        else:
            return 'Unknown Error'

    def get_station_by_latlng(self, lat, lng):
        r = requests.get(self._url(f'/feed/geo:{lat};{lng}/'),
                         params=self.params)
        if r.json()['status'] == 'ok':
            return Station(r.json()['data'])
        elif r.json()['status'] == 'error':
            return (r.json()['status'], r.json()['message'])
        else:
            return 'Unknown Error'

    # TODO(danoscarmike): what is the best format to pass a bounding box?
    # Is there a standard?
    def list_stations_by_bbox(self, lat1, lng1, lat2, lng2, complete=False):
        bbox = [min(lat1, lat2), min(lng1, lng2), max(lat1, lat2),
                max(lng1, lng2)]
        latlng = (',').join(list(map(str, bbox)))
        r = requests.get(self._url(f'/map/bounds/?latlng={latlng}'),
                         params=self.params)
        if r.json()['status'] == 'ok':
            stations_locs = [Location(station) for station in r.json()['data']]
            if complete:
                return [self.get_station_by_city_name(f'@{loc.uid}')
                        for loc in stations_locs]
            else:
                return stations_locs
        elif r.json()['status'] == 'error':
            return (r.json()['status'], r.json()['message'])
        else:
            return 'Unknown Error'

    def list_stations_by_keyword(self, keyword):
        r = requests.get(self._url(f'search/?keyword={keyword}'),
                         params=self.params)
        if r.json()['status'] == 'ok':
            stations = [result['uid'] for result in r.json()['data']]
            return [self.get_station_by_city_name(f'@{station}')
                    for station in stations]
        elif r.json()['status'] == 'error':
            return (r.json()['status'], r.json()['message'])
        else:
            return 'Unknown Error'
