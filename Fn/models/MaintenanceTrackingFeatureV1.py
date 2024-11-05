from typing import *

from pydantic import BaseModel, Field

from .LineString import LineString
from .MaintenanceTrackingPropertiesV1 import MaintenanceTrackingPropertiesV1
from .MultiLineString import MultiLineString
from .MultiPoint import MultiPoint
from .MultiPolygon import MultiPolygon
from .Point import Point
from .Polygon import Polygon


class MaintenanceTrackingFeatureV1(BaseModel):
    """
    None model
        GeoJSON Feature Object of maintenance tracking.

    """

    type: str = Field(alias="type")

    properties: MaintenanceTrackingPropertiesV1 = Field(alias="properties")

    geometry: Union[LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon] = Field(alias="geometry")
