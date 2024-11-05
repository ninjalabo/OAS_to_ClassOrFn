from typing import *

from pydantic import BaseModel, Field


class TrafficMessageRoadAddressV1(BaseModel):
    """
    None model
        Location in road address (road number + number of the road section + distance from the beginning of the road section

    """

    road: int = Field(alias="road")

    roadSection: int = Field(alias="roadSection")

    distance: int = Field(alias="distance")
