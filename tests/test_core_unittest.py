from context import core
from waqi_python import station


import unittest


class TestCore(unittest.TestCase):

    def test_get_station_by_path(self):
        client = core.WaqiClient()
        response = client.get_station_by_path('shanghai')
        self.assertTrue(isinstance(response, station.Station),
                        'Should return instance of Station class')

    def test_get_station_by_id(self):
        client = core.WaqiClient()
        response = client.get_station_by_id('1437')
        self.assertTrue(isinstance(response, station.Station),
                        'Should return instance of Station class')

    def test_get_local_station(self):
        client = core.WaqiClient()
        response = client.get_local_station()
        self.assertTrue(isinstance(response, station.Station),
                        'Should return instance of Station class')

    def test_get_station_by_latlng(self):
        # Pass arbitrary location (in Ireland)
        # Expect response['data'] to be populated
        client = core.WaqiClient()
        response = client.get_station_by_latlng(53.1, -7.4)
        self.assertTrue(isinstance(response, station.Station),
                        'Should return instance of Station class')

    def test_list_stations_by_bbox(self):
        # Pass arbitrary location (bounding box of New South Wales, Australia)
        # Expect response['data'] to be populated
        client = core.WaqiClient()
        response = client.list_stations_by_bbox(-37.6, 140.5, -27.9, 154.1)
        self.assertTrue(len(response) > 0, 'Payload should contain data.')


    def test_get_stations_by_bbox_expect_empty(self):
        # Pass arbitrary location (bounding box in Coral Sea)
        # Expect response['data'] to be empty
        client = core.WaqiClient()
        response = client.list_stations_by_bbox(-27.9, 154.1, -27.7, 154.2)
        self.assertTrue(response is None, 'Payload should be empty.')


    def test_list_stations_by_keyword(self):
        client = core.WaqiClient()
        response = client.list_stations_by_keyword('beijing')
        self.assertTrue(len(response) > 0, 'Payload should contain data.')


if __name__ == '__main__':
    unittest.main()
