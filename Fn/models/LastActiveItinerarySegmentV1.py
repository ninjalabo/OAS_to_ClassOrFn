from typing import *

from pydantic import BaseModel, Field

from .ItineraryLegV1 import ItineraryLegV1


class LastActiveItinerarySegmentV1(BaseModel):
    """
    None model
        The itinerary segment of this special transport that is or was last active.

    """

    startTime: str = Field(alias="startTime")

    endTime: str = Field(alias="endTime")

    legs: List[ItineraryLegV1] = Field(alias="legs")
