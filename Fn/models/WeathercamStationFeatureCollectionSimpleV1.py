from typing import *

from pydantic import BaseModel, Field

from .WeathercamStationFeatureSimpleV1 import WeathercamStationFeatureSimpleV1


class WeathercamStationFeatureCollectionSimpleV1(BaseModel):
    """
    None model
        Weathercam GeoJSON FeatureCollection object with basic information

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[WeathercamStationFeatureSimpleV1] = Field(alias="features")
