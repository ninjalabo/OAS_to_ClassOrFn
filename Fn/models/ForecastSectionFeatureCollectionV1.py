from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionFeatureV1 import ForecastSectionFeatureV1


class ForecastSectionFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON feature collection of forecast sections

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[ForecastSectionFeatureV1] = Field(alias="features")
