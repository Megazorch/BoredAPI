"""
Activity instance
"""
from typing import Optional


class Activity:
    """
    Activity class
    """

    # Constructor
    # activity_data: dict
    #     The activity data from the Bored API

    def __init__(self, activity_data: Optional[dict] = None):
        self.activity_data = activity_data
        self.activity = ''

    def __str__(self) -> str:
        """
        Return the activity data as a string.
        """
        if self.activity_data is None:
            return "No activity data"

        for key, value in self.activity_data.items():
            self.activity += f"{key}: {value} \n"
        return self.activity
