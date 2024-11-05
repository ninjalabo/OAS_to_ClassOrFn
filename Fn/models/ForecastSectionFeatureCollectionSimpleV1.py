from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionFeatureSimpleV1 import ForecastSectionFeatureSimpleV1


class ForecastSectionFeatureCollectionSimpleV1(BaseModel):
    """
    None model
        GeoJSON feature collection of simple forecast sections

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[ForecastSectionFeatureSimpleV1] = Field(alias="features")
