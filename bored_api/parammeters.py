"""
GetActivityParams class
"""
import logging
from typing import Optional
from dataclasses import dataclass

logger = logging.getLogger("bored_api")


@dataclass
class GetActivityParams:
    """
    Class to hold parameters for the get_activity method
    """
    action: Optional[str] = None,
    activity_type: Optional[str] = None,
    participants: Optional[int] = None,
    price: Optional[float] = None,
    minprice: Optional[float] = None,
    maxprice: Optional[float] = None,
    accessibility: Optional[float] = None,
    minaccessibility: Optional[float] = None,
    maxaccessibility: Optional[float] = None

    logger.info("Initialized GetActivityParams")

    def __str__(self):
        return f"activity_type: {self.activity_type}, " \
               f"participants: {self.participants}, " \
               f"price: {self.price}, " \
               f"minprice: {self.minprice}, " \
               f"maxprice: {self.maxprice}, " \
               f"accessibility: {self.accessibility}, " \
               f"minaccessibility: {self.minaccessibility}, " \
               f"maxaccessibility: {self.maxaccessibility}"

    def to_dict(self):
        """
        Return the parameters as a dictionary.
        :return:
        """
        return {
            "type": self.activity_type,
            "participants": self.participants,
            "price": self.price,
            "minprice": self.minprice,
            "maxprice": self.maxprice,
            "accessibility": self.accessibility,
            "minaccessibility": self.minaccessibility,
            "maxaccessibility": self.maxaccessibility
        }
