"""
Test for Activity object
"""
import unittest
from database.activity import Activity


class ActivityObjectTest(unittest.TestCase):
    """
    Testing Activity object
    """
    def setUp(self):
        self.activity_data = {
            "activity": "Write a song",
            "type": "music",
            "participants": 1,
            "price": 0,
            "link": "www.youtube.com",
            "key": "key",
            "accessibility": 0.5
        }

    def test_activity_object_creation(self):
        """
        Testing Activity object
        :return:
        """
        activity = Activity(self.activity_data)
        self.assertEqual(activity.activity, "Write a song")
        self.assertEqual(activity.activity_type, "music")
        self.assertEqual(activity.participants, 1)
        self.assertEqual(activity.price, 0)
        self.assertEqual(activity.link, "www.youtube.com")
        self.assertEqual(activity.key, "key")
        self.assertEqual(activity.accessibility, 0.5)


if __name__ == '__main__':
    unittest.main()
