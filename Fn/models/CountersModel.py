from typing import *

from pydantic import BaseModel, Field

from .CounterFeatureModel import CounterFeatureModel


class CountersModel(BaseModel):
    """
    None model
        GeoJson FeatureCollection

    """

    features: List[CounterFeatureModel] = Field(alias="features")

    type: str = Field(alias="type")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)
