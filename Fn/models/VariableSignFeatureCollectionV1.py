from typing import *

from pydantic import BaseModel, Field

from .VariableSignFeatureV1 import VariableSignFeatureV1


class VariableSignFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of variable signs

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[VariableSignFeatureV1] = Field(alias="features")
