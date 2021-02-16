from unittest import TestCase
from file_duplicator import api_handler
import sys

sys.tracebacklimit = 0


class TestGetApiData(TestCase):
    def test_valid_endpoint(self):
        result = api_handler.get_api_data('https://randomuser.me/api/?nat=us&results=1')
        self.assertIsNotNone(result)

    def test_invalid_endpoint(self):
        result = api_handler.get_api_data('https://randomuser.m3/api/?nat=us&results=1')
        self.assertIsNone(result)
