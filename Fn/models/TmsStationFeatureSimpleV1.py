from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .TmsStationPropertiesSimpleV1 import TmsStationPropertiesSimpleV1


class TmsStationFeatureSimpleV1(BaseModel):
    """
    None model
        Tms station GeoJSON Feature object with basic information

    """

    type: str = Field(alias="type")

    id: int = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: TmsStationPropertiesSimpleV1 = Field(alias="properties")
