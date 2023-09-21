import unittest
from bored_api.parammeters import GetActivityParams


class GetActivityParamsTest(unittest.TestCase):
    """
    Class to test GetActivityParams class
    """
    def setUp(self) -> None:
        self.params = {'action': 'new',
                       'activity_type': 'education',
                       'participants': 1,
                       'price': 0.5,
                       'minprice': 0.5,
                       'maxprice': 0.5,
                       'accessibility': 0.5,
                       'minaccessibility': 0.5,
                       'maxaccessibility': 0.5,
                       'verbose': False}

        self.result = {'type': 'education',
                       'participants': 1,
                       'price': 0.5,
                       'minprice': 0.5,
                       'maxprice': 0.5,
                       'accessibility': 0.5,
                       'minaccessibility': 0.5,
                       'maxaccessibility': 0.5
                       }

    def test_to_dict(self):
        parameters = GetActivityParams(**self.params)
        self.assertEqual(parameters.to_dict(), self.result)


if __name__ == '__main__':
    unittest.main()
