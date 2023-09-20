"""
Main functions for the API
"""
import requests
import logging
from bored_api.parammeters import GetActivityParams

logger = logging.getLogger("bored_api")


class BoredApiClient:
    """
    Class for the Bored API
    """
    base_url = "https://www.boredapi.com/api/"

    def get_activity(self,  parameters: GetActivityParams) -> dict:
        """
        Get an activity from the Bored API
        :return r.json():
        """
        url = self.base_url + "activity"

        try:
            logger.info("Fetching activity from Bored API")
            logger.debug(f"Fetching activity from Bored API with parameters: {parameters}")
            response = requests.get(url, params=parameters.to_dict())

            if response.status_code == 200:
                activity_data = response.json()
                logger.info(f"Fetched activity from Bored API: {activity_data}")
                return activity_data
            else:
                logger.error(f"Failed to fetch activity. Status code: {response.status_code}")
                logger.info("Finished")

        except Exception as e:
            logger.error(f"Failed to fetch activity. Error: {str(e)}")
            logger.info("Finished")

    @staticmethod
    def check_activity(activity: dict) -> bool:
        """
        Check the response from the Bored API
        :return bool:
        """
        keys = activity.keys()

        if "activity" in keys:
            return True
        elif "error" in keys:
            return False
