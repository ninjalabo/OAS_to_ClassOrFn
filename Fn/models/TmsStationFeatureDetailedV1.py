from typing import *

from pydantic import BaseModel, Field

from .Point import Point
from .TmsStationPropertiesDetailedV1 import TmsStationPropertiesDetailedV1


class TmsStationFeatureDetailedV1(BaseModel):
    """
    None model
         Tms station GeoJSON feature object with detailed information

    """

    type: str = Field(alias="type")

    id: int = Field(alias="id")

    geometry: Point = Field(alias="geometry")

    properties: TmsStationPropertiesDetailedV1 = Field(alias="properties")
