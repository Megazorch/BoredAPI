"""
Activity instance
"""


class Activity:
    """
    Activity class
    """

    # Constructor
    # activity_data: dict
    #     The activity data from the Bored API

    def __init__(self, activity_data: dict):
        self.activity_data = activity_data
        self.activity = ''

    def __str__(self):
        for key, value in self.activity_data.items():
            self.activity += f"{key}: {value} \n"
        return self.activity

    def dict(self) -> dict:
        """
        Return the activity data as a dictionary.
        :return activity_data: dict
            The activity data as a dictionary.
        """
        return self.activity_data
