from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .WeatherStationPropertiesSimpleV1 import WeatherStationPropertiesSimpleV1


class WeatherStationFeatureSimpleV1(BaseModel):
    """
    None model
        Weather station GeoJSON Feature object with basic information

    """

    type: str = Field(alias="type")

    id: int = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: WeatherStationPropertiesSimpleV1 = Field(alias="properties")
