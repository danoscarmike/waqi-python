import requests

from base_client import BaseClient


class WaqiClient(BaseClient):
    def _url(self, path):
        return self.base_url + path


    def get_city_feed(self, city):
        r = requests.get(self._url(f'feed/{city}/?token={self.token}'))
        return r, r.json()


    def get_local_feed(self):
        r = requests.get(self._url(f'feed/here/?token={self.token}'))
        return r, r.json()


    def get_feed_by_location(lat, lng):
        r = requests.get(self._url(f'/feed/geo:{lat};{lng}/?token={self.token}'))
        return r, r.json()


    # TODO(danoscarmike): what is the best format to pass a bounding box?
    # Is there a standard?
    def get_stations_in_bounds(lat1, lng1, lat2, lng2):
        latlng = (',').join(list(map(str, [lat1, lng1, lat2, lng2])))
        r = requests.get(self._url(f'/map/bounds/?token={self.token}&latlng={latlng}'))
        return r, r.json()


    def search_stations(keyword):
        r = requests.get(self._url(f'search/?keyword={keyword}&token={self.token}'))
        return r, r.json()
