"""
Activity instance
"""
from typing import Optional


class Activity:
    """
    Activity class
    """
    def __init__(self, activity_data: dict = None):
        try:
            self.activity = activity_data['activity']
            self.activity_type = activity_data['type']
            self.participants = activity_data['participants']
            self.price = activity_data['price']
            self.link = activity_data['link']
            self.key = activity_data['key']
            self.accessibility = activity_data['accessibility']
        except KeyError or TypeError:
            self.activity = None
            self.activity_type = None
            self.participants = None
            self.price = None
            self.link = None
            self.key = None
            self.accessibility = None

    def __str__(self) -> str:
        """
        Return the activity data as a string.
        """
        if self.activity is None:
            return "No activity data"
        else:
            return f"Activity: {self.activity}\n" \
                   f"Type: {self.activity_type}\n" \
                   f"Participants: {self.participants}\n" \
                   f"Price: {self.price}\n" \
                   f"Link: {self.link}\n" \
                   f"Key: {self.key}\n" \
                   f"Accessibility: {self.accessibility}\n"

