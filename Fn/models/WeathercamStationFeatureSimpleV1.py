from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .WeathercamStationPropertiesSimpleV1 import WeathercamStationPropertiesSimpleV1


class WeathercamStationFeatureSimpleV1(BaseModel):
    """
    None model
        Weathercam station GeoJSON Feature object with basic information

    """

    type: str = Field(alias="type")

    id: str = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: WeathercamStationPropertiesSimpleV1 = Field(alias="properties")
