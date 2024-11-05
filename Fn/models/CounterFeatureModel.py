from typing import *

from pydantic import BaseModel, Field

from .CounterModel import CounterModel


class CounterFeatureModel(BaseModel):
    """
    None model
        GeoJson Feature

    """

    geometry: Dict[str, Any] = Field(alias="geometry")

    type: str = Field(alias="type")

    properties: CounterModel = Field(alias="properties")
