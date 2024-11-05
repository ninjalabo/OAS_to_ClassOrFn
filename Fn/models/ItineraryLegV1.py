from typing import *

from pydantic import BaseModel, Field

from .ItineraryRoadLegV1 import ItineraryRoadLegV1


class ItineraryLegV1(BaseModel):
    """
    None model
        ItineraryLeg is one leg of the route

    """

    roadLeg: Optional[ItineraryRoadLegV1] = Field(alias="roadLeg", default=None)

    streetName: Optional[str] = Field(alias="streetName", default=None)
