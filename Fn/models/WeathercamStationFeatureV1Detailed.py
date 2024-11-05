from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .WeathercamStationPropertiesDetailedV1 import WeathercamStationPropertiesDetailedV1


class WeathercamStationFeatureV1Detailed(BaseModel):
    """
    None model
         Weathercam station GeoJSON feature object with detailed information

    """

    type: str = Field(alias="type")

    id: str = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: WeathercamStationPropertiesDetailedV1 = Field(alias="properties")
