import requests

from .base_client import BaseClient
from .station import Station


class WaqiClient(BaseClient):
    def _url(self, path):
        return self.base_url + path


    def get_city_feed(self, city):
        r = requests.get(self._url(f'feed/{city}/'), params=self.params)
        # return r, r.json()
        if r.json()['status'] == 'ok':
            return Station(r.json()['data'])


    def get_local_feed(self):
        r = requests.get(self._url(f'feed/here/'), params=self.params)
        return r, r.json()


    def get_feed_by_location(self, lat, lng):
        r = requests.get(self._url(f'/feed/geo:{lat};{lng}/'),
                         params=self.params)
        return r, r.json()


    # TODO(danoscarmike): what is the best format to pass a bounding box?
    # Is there a standard?
    def get_stations_in_bounds(self, lat1, lng1, lat2, lng2):
        latlng = (',').join(list(map(str, [lat1, lng1, lat2, lng2])))
        r = requests.get(self._url(f'/map/bounds/?latlng={latlng}'),
                         params=self.params)
        return r, r.json()


    def search_stations(self, keyword):
        r = requests.get(self._url(f'search/?keyword={keyword}'),
                         params=self.params)
        return r, r.json()
