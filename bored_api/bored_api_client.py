"""
Main functions for the API
"""
import logging
import requests
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

        # Specify a timeout (in seconds)
        timeout_seconds = 10

        try:
            logger.info("Fetching activity from Bored API")
            logger.debug(f"Fetching activity from Bored API with parameters: {parameters}")
            response = requests.get(url, params=parameters.to_dict(), timeout=timeout_seconds)

            if response.status_code == 200:
                activity_data = response.json()
                logger.info(f"Fetched activity from Bored API: {activity_data}")
                return activity_data

            logger.error(f"Failed to fetch activity. Status code: {response.status_code}")
            logger.info("Finished")
            return {}

        except requests.Timeout:
            logger.error(f"Request timed out after {timeout_seconds} seconds.")
            logger.info("Finished")
            return {}

        except requests.RequestException as exc:
            logger.error(f"Failed to fetch activity. Error: {str(exc)}")
            logger.info("Finished")
            return {}

    @staticmethod
    def check_activity(activity: dict) -> bool:
        """
        Check the response from the Bored API
        :return bool:
        """
        keys = activity.keys()

        return True if "activity" in keys else False
