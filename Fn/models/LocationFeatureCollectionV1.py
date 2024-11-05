from typing import *

from pydantic import BaseModel, Field

from .LocationFeatureV1 import LocationFeatureV1


class LocationFeatureCollectionV1(BaseModel):
    """
    None model
        Location GeoJSON feature collection object

    """

    type: str = Field(alias="type")

    locationsVersion: str = Field(alias="locationsVersion")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[LocationFeatureV1] = Field(alias="features")
