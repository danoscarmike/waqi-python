from .context import client as base
from waqi_python.objects import *
from waqi_python.exceptions import *


import unittest
from unittest.mock import Mock, patch


class TestClient(unittest.TestCase):

    def test_get_station_by_path(self):
        client = base.WaqiClient()
        response = client.get_station_by_path('shanghai')
        self.assertTrue(isinstance(response, Station),
                        'Should return instance of Station class')

    def test_get_station_by_id(self):
        client = base.WaqiClient()
        response = client.get_station_by_id('1437')
        self.assertTrue(isinstance(response, Station),
                        'Should return instance of Station class')

    def test_get_local_station(self):
        client = base.WaqiClient()
        response = client.get_local_station()
        self.assertTrue(isinstance(response, Station),
                        'Should return instance of Station class')

    def test_get_station_by_latlng(self):
        # Pass arbitrary location (in Ireland)
        # Expect response['data'] to be populated
        client = base.WaqiClient()
        response = client.get_station_by_latlng(53.1, -7.4)
        self.assertTrue(isinstance(response, Station),
                        'Should return instance of Station class')

    def test_list_stations_by_bbox(self):
        # Pass arbitrary location (bounding box of New South Wales, Australia)
        # Expect response['data'] to be populated
        client = base.WaqiClient()
        response = client.list_stations_by_bbox(-37.6, 140.5, -27.9, 154.1)
        self.assertTrue(len(response) > 0, 'Payload should contain data.')


    def test_get_stations_by_bbox_expect_empty(self):
        # Pass arbitrary location (bounding box in Coral Sea)
        # Expect response['data'] to be empty
        client = base.WaqiClient()
        response = client.list_stations_by_bbox(-27.9, 154.1, -27.7, 154.2)
        self.assertTrue(response == [], 'Payload should be empty.')


    def test_list_stations_by_keyword(self):
        client = base.WaqiClient()
        response = client.list_stations_by_keyword('beijing')
        self.assertTrue(len(response) > 0, 'Payload should contain data.')


    def test_bad_datetime(self):
        bad_data = {'tz':'Somewhere', 's':'Somemonth/Someday/Someyear'}
        bad_time = Time(bad_data)
        self.assertTrue(bad_time.datetime is None, 'Datetime should be None.')


    @patch('waqi_python.client.requests.get')
    def test_non_200_ApiError(self, mock_get):
        mock_get.return_value.ok = False
        client = base.WaqiClient()
        with self.assertRaises(ApiError):
            response = client.get_local_station()


    @patch('waqi_python.client.requests.get')
    def test_200_but_error_message(self, mock_get):
        error_response = {"status": "error", "message": "<error-response>"}
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = error_response
        client = base.WaqiClient()
        with self.assertRaises(ApiError):
            response = client.get_local_station()


    @patch('waqi_python.client.requests.get')
    def test_200_unknown_message(self, mock_get):
        error_response = {"status": "some unclear weirdness", "error": "weird"}
        mock_get.return_value = Mock(status_code=200)
        mock_get.return_value.json.return_value = error_response
        client = base.WaqiClient()
        with self.assertRaises(UnknownError):
            response = client.get_local_station()


if __name__ == '__main__':
    unittest.main()
