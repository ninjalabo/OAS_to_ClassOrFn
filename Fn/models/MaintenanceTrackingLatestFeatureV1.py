from typing import *

from pydantic import BaseModel, Field

from .LineString import LineString
from .MaintenanceTrackingLatestPropertiesV1 import MaintenanceTrackingLatestPropertiesV1
from .MultiLineString import MultiLineString
from .MultiPoint import MultiPoint
from .MultiPolygon import MultiPolygon
from .Point import Point
from .Polygon import Polygon


class MaintenanceTrackingLatestFeatureV1(BaseModel):
    """
    None model
        GeoJSON Feature Object of latest maintenance tracking.

    """

    type: str = Field(alias="type")

    properties: MaintenanceTrackingLatestPropertiesV1 = Field(alias="properties")

    geometry: Union[LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon] = Field(alias="geometry")
