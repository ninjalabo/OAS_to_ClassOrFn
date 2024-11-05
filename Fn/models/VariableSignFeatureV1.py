from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .VariableSignPropertiesV1 import VariableSignPropertiesV1


class VariableSignFeatureV1(BaseModel):
    """
    None model
        GeoJSON Feature Object of variable sign

    """

    type: str = Field(alias="type")

    geometry: Point = Field(alias="geometry")

    properties: VariableSignPropertiesV1 = Field(alias="properties")
