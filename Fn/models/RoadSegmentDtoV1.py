from typing import *

from pydantic import BaseModel, Field


class RoadSegmentDtoV1(BaseModel):
    """
    None model
        Forecast section road segments. Refers to https://aineistot.vayla.fi/digiroad/

    """

    startDistance: Optional[int] = Field(alias="startDistance", default=None)

    endDistance: Optional[int] = Field(alias="endDistance", default=None)

    carriageway: Optional[int] = Field(alias="carriageway", default=None)
