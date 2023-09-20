"""
Main functions for the API
"""
import requests
import logging


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
            logging.info("Fetching activity from Bored API")
            logging.debug(f"Fetching activity from Bored API with parameters: {parameters}")
            response = requests.get(url, params=parameters)

            if response.status_code == 200:
                activity_data = response.json()
                logging.info(f"Fetched activity from Bored API: {activity_data}")
                return activity_data
            else:
                logging.error(f"Failed to fetch activity. Status code: {response.status_code}")
                logging.info("Finished")

        except Exception as e:
            logging.error(f"Failed to fetch activity. Error: {str(e)}")
            logging.info("Finished")
