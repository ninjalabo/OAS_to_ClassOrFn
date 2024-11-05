from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionPropertiesSimpleV1 import ForecastSectionPropertiesSimpleV1
from .LineString import LineString


class ForecastSectionFeatureSimpleV1(BaseModel):
    """
    None model
        GeoJSON feature object of simple forecast section

    """

    type: str = Field(alias="type")

    id: str = Field(alias="id")

    geometry: LineString = Field(alias="geometry")

    properties: ForecastSectionPropertiesSimpleV1 = Field(alias="properties")
