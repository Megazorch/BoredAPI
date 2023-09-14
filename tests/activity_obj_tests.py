import unittest
from models.activity import Activity


class ActivityObjectTest(unittest.TestCase):
    def SetUp(self):
        self.activity_data = {
            "action": "new",
            "type": "music",
            "participants": 1,
            "price": 0,
            "link": "www.youtube.com",
            "key": "key"

        }
    def test_activity_object_creation(self):
        activity = Activity()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
