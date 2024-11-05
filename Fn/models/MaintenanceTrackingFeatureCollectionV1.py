from typing import *

from pydantic import BaseModel, Field

from .MaintenanceTrackingFeatureV1 import MaintenanceTrackingFeatureV1


class MaintenanceTrackingFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of maintenance trackings

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[MaintenanceTrackingFeatureV1] = Field(alias="features")
