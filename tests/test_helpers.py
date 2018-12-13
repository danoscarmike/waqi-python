import unittest

from waqi_python.objects import *


class TestHelpers(unittest.TestCase):

    def test_bad_datetime(self):
        bad_data = {'tz':'Somewhere', 's':'Somemonth/Someday/Someyear'}
        bad_time = Time(bad_data)
        self.assertTrue(bad_time.datetime is None, 'Datetime should be None.')
