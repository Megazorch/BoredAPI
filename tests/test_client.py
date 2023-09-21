"""
Unit tests for BoredApiClient class
"""
import unittest
from bored_api.bored_api_client import BoredApiClient
from bored_api.parammeters import GetActivityParams


class BoredApiClientTest(unittest.TestCase):
    """
    Class for testing BoredApiClient class
    """
    def setUp(self):
        self.bored_api_client = BoredApiClient()
        self.params = {'action': 'new',
                       'activity_type': 'music',
                       'participants': 1,
                       'price': None,
                       'minprice': None,
                       'maxprice': None,
                       'accessibility': None,
                       'minaccessibility': None,
                       'maxaccessibility': None,
                       'verbose': False}
        self.get_activity_params = GetActivityParams(**self.params)

    def test_get_activity(self):
        """
        Test get_activity method
        :return:
        """
        activity = self.bored_api_client.get_activity(self.get_activity_params)
        self.assertIsNotNone(activity)
        self.assertIsNotNone(activity['activity'])
        self.assertIsNotNone(activity['type'])
        self.assertIsNotNone(activity['participants'])
        self.assertIsNotNone(activity['price'])
        self.assertIsNotNone(activity['link'])
        self.assertIsNotNone(activity['key'])
        self.assertIsNotNone(activity['accessibility'])

    def test_check_activity(self):
        """
        Test check_activity method
        :return:
        """
        activity = self.bored_api_client.check_activity(self.get_activity_params)
        self.assertTrue(activity)


if __name__ == '__main__':
    unittest.main()
