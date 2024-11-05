from typing import *

from pydantic import BaseModel, Field

from .RegionGeometryFeatureV1 import RegionGeometryFeatureV1


class RegionGeometryFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of Region Geometries

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[RegionGeometryFeatureV1] = Field(alias="features")
