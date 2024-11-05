from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .WeatherStationPropertiesDetailedV1 import WeatherStationPropertiesDetailedV1


class WeatherStationFeatureDetailedV1(BaseModel):
    """
    None model
        Weather station GeoJSON feature object with detailed information

    """

    type: str = Field(alias="type")

    id: int = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: WeatherStationPropertiesDetailedV1 = Field(alias="properties")
