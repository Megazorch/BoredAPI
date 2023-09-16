import unittest
from models.activity import Activity


class ActivityObjectTest(unittest.TestCase):
    def setUp(self):
        self.activity_data = {
            "action": "new",
            "type": "music",
            "participants": 1,
            "price": 0,
            "link": "www.youtube.com",
            "key": "key"
        }

    def test_activity_object_creation(self):
        """
        Testing Activity object
        :return:
        """
        activity = Activity(self.activity_data)
        self.assertEqual(activity.dict(), self.activity_data)
        self.assertEqual(activity.activity_data['action'], "new")


if __name__ == '__main__':
    unittest.main()
