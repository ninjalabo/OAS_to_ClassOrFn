from typing import *

from pydantic import BaseModel, Field

from .LineString import LineString
from .MultiLineString import MultiLineString
from .MultiPoint import MultiPoint
from .MultiPolygon import MultiPolygon
from .Point import Point
from .Polygon import Polygon
from .RegionGeometryPropertiesV1 import RegionGeometryPropertiesV1


class RegionGeometryFeatureV1(BaseModel):
    """
    None model
        Region area GeoJSON Feature object

    """

    type: str = Field(alias="type")

    geometry: Union[LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon] = Field(alias="geometry")

    properties: RegionGeometryPropertiesV1 = Field(alias="properties")
