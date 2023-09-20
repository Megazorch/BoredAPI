"""
Action for main.py
"""
import logging
from dataclasses import dataclass
from actions.console_printer import ConsolePrinter
from bored_api.parammeters import GetActivityParams
from bored_api.bored_api_client import BoredApiClient
from database.activity_repository import ActivityRepository
from database.activity import Activity

logger = logging.getLogger("bored_api")


@dataclass
class NewAction:
    """
    Class to handle the new action
    """
    client: BoredApiClient
    repository: ActivityRepository
    printer: ConsolePrinter

    def __call__(self, parameters: GetActivityParams):
        # Get an activity
        activity = self.client.get_activity(parameters)

        # Check the response from the Bored API
        activity_check = self.client.check_activity(activity)

        if activity_check is True:
            # Store activity in Activity class
            activity = Activity(activity)

            # Add activity to database
            new_activity = self.repository.save(activity)

            # Print message to the console
            self.printer.message_to_user(new_activity)

            # Finish logging
            logger.info('Finished')

        else:
            self.printer.error_response_from_api(activity)

@dataclass
class ListAction:
    """
    Class to handle the list action
    """
    repository: ActivityRepository
    printer: ConsolePrinter

    def __call__(self, parameters: GetActivityParams):
        # List last 5 activities from database
        last_five_activities = self.repository.find_last_five()

        # Print message to the console
        self.printer.message_to_user(last_five_activities)

        # Finish logging
        logger.info('Finished')
