from typing import *

from pydantic import BaseModel, Field

from .TmsStationFeatureSimpleV1 import TmsStationFeatureSimpleV1


class TmsStationFeatureCollectionSimpleV1(BaseModel):
    """
    None model
        GeoJSON feature collection of TMS stations

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[TmsStationFeatureSimpleV1] = Field(alias="features")
