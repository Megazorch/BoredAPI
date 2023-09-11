"""
Main functions for the API
"""
import requests


class BoredApiManager:
    """
    Class for the Bored API
    """
    def __init__(self, parameters=None):
        self.parameters = parameters

    def get_activity(self):
        """
        Download image.
        :return r.json():
        """
        url = "https://www.boredapi.com/api/activity"
        try:
            response = requests.get(url, params=self.parameters)

            if response.status_code == 200:
                activity_data = response.json()
                return activity_data
            else:
                return {"error": f"Failed to fetch activity. Status code: {response.status_code}"}

        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
