"""
Main functions for the API
"""
import requests


class BoredApiClient:
    """
    Class for the Bored API
    """
    base_url = "https://www.boredapi.com/api/"

    def get_activity(self,  parameters: dict = None) -> dict:
        """
        Get an activity from the Bored API
        :return r.json():
        """
        url = self.base_url + "activity"

        try:
            response = requests.get(url, params=parameters)

            if response.status_code == 200:
                activity_data = response.json()
                return activity_data
            else:
                return {"error": f"Failed to fetch activity. Status code: {response.status_code}"}

        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
