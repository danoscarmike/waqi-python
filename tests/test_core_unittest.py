from context import core

import unittest


class TestCore(unittest.TestCase):

    def test_get_city_feed(self):
        response, payload = core.get_city_feed('shanghai')
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')
        self.assertTrue(len(payload['data']) > 0, 'Should contain data.')

    def test_get_local_feed(self):
        response, payload = core.get_local_feed()
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')

    def test_get_feed_by_location(self):
        # Pass arbitrary location (in Ireland)
        # Expect response['data'] to be populated
        response, payload = core.get_feed_by_location(53.1, -7.4)
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')
        self.assertTrue(len(payload['data']) > 0, 'Should contain data.')

    def test_get_stations_in_bounds(self):
        # Pass arbitrary location (bounding box of New South Wales, Australia)
        # Expect response['data'] to be populated
        response, payload = core.get_stations_in_bounds(-37.6, 140.5,
                                                        -27.9, 154.1)
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')
        self.assertTrue(len(payload['data']) > 0,
                        'Payload should contain data.')


    def test_get_stations_in_bounds_expect_empty(self):
        # Pass arbitrary location (bounding box in Coral Sea)
        # Expect response['data'] to be empty
        response, payload = core.get_stations_in_bounds(-27.9, 154.1,
                                                        -27.7, 154.2)
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')
        self.assertTrue(len(payload['data']) == 0, 'Payload should be empty.')


    def test_search_stations(self):
        response, payload = core.search_stations('san francisco')
        self.assertEqual(response.status_code, 200, 'Should be 200.')
        self.assertTrue('status' in payload, 'Payload should include "status".')
        self.assertTrue('data' in payload, 'Payload should include "data".')
        self.assertTrue(len(payload['data']) > 0,
                        'Payload should contain data.')


if __name__ == '__main__':
    unittest.main()
