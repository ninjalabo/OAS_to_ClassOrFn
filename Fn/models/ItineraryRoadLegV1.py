from typing import *

from pydantic import BaseModel, Field


class ItineraryRoadLegV1(BaseModel):
    """
    None model
        ItineraryRoadLeg is route leg that is on the road network.

    """

    roadNumber: Optional[int] = Field(alias="roadNumber", default=None)

    roadName: Optional[str] = Field(alias="roadName", default=None)

    startArea: Optional[str] = Field(alias="startArea", default=None)

    endArea: Optional[str] = Field(alias="endArea", default=None)
