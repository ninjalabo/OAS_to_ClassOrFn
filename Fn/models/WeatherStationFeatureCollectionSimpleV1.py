from typing import *

from pydantic import BaseModel, Field

from .WeatherStationFeatureSimpleV1 import WeatherStationFeatureSimpleV1


class WeatherStationFeatureCollectionSimpleV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of weather stations

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[WeatherStationFeatureSimpleV1] = Field(alias="features")
