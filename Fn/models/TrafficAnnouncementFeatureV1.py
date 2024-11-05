from typing import *

from pydantic import BaseModel, Field

from .LineString import LineString
from .MultiLineString import MultiLineString
from .MultiPoint import MultiPoint
from .MultiPolygon import MultiPolygon
from .Point import Point
from .Polygon import Polygon
from .TrafficAnnouncementPropertiesV1 import TrafficAnnouncementPropertiesV1


class TrafficAnnouncementFeatureV1(BaseModel):
    """
    None model
        TrafficAnnouncement GeoJSON Feature Object

    """

    type: str = Field(alias="type")

    geometry: Union[LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon] = Field(alias="geometry")

    properties: TrafficAnnouncementPropertiesV1 = Field(alias="properties")
