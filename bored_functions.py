"""
Main functions for the API
"""
import requests

type_of_activity = ''
"""
Type of the activity
["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
"""

participants = 0
"""
The number of people that this activity could involve
[0, n]
"""

price = 0.0
price_min = 0.0
price_max = 0.0
"""
A factor describing the cost of the event with zero being free
[0, 1]
"""

accessibility = 0.0
accessibility_min = 0.0
accessibility_max = 0.0
"""
A factor describing how possible an event is to do with zero being the most accessible
[0.0, 1.0]
"""

def get_activity(parameters=None):
    """
    Download image.
    :return r.json():
    """
    url = "https://www.boredapi.com/api/activity?"
    # tags = {'included_tags': included_tags, 'is_nsfw': is_nsfw, 'many': many}
    r = requests.get(url, params=parameters)

    return r.json()

param = {'type': 'recreational'}
print(get_activity(param))
