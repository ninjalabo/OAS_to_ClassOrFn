from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionPropertiesV1 import ForecastSectionPropertiesV1
from .LineString import LineString
from .MultiLineString import MultiLineString
from .MultiPoint import MultiPoint
from .MultiPolygon import MultiPolygon
from .Point import Point
from .Polygon import Polygon


class ForecastSectionFeatureV1(BaseModel):
    """
    None model
        GeoJSON feature object of forecast section

    """

    type: str = Field(alias="type")

    id: Optional[str] = Field(alias="id", default=None)

    geometry: Union[LineString, MultiLineString, MultiPoint, MultiPolygon, Point, Polygon] = Field(alias="geometry")

    properties: ForecastSectionPropertiesV1 = Field(alias="properties")
