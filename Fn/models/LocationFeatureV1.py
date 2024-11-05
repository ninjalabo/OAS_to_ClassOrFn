from typing import *

from pydantic import BaseModel, Field

from .LocationPropertiesV1 import LocationPropertiesV1
from .Point import Point


class LocationFeatureV1(BaseModel):
    """
    None model
        Location GeoJSON feature object

    """

    type: str = Field(alias="type")

    id: int = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: LocationPropertiesV1 = Field(alias="properties")
