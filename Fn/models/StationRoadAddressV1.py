from typing import *

from pydantic import BaseModel, Field


class StationRoadAddressV1(BaseModel):
    """
    None model
        Road station road address

    """

    roadNumber: Optional[int] = Field(alias="roadNumber", default=None)

    roadSection: Optional[int] = Field(alias="roadSection", default=None)

    distanceFromRoadSectionStart: Optional[int] = Field(alias="distanceFromRoadSectionStart", default=None)

    carriageway: Optional[str] = Field(alias="carriageway", default=None)

    side: Optional[str] = Field(alias="side", default=None)

    contractArea: Optional[str] = Field(alias="contractArea", default=None)

    contractAreaCode: Optional[int] = Field(alias="contractAreaCode", default=None)
