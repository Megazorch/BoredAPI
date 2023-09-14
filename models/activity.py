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

    def to_tuple(self):
        return (self.activity_data['activity'],
                self.activity_data['type'],
                self.activity_data['participants'],
                self.activity_data['price'],
                self.activity_data['link'],
                self.activity_data['key'],
                self.activity_data['accessibility']
                )
