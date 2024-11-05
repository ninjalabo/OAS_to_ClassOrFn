from typing import *

from pydantic import BaseModel, Field

from .MaintenanceTrackingLatestFeatureV1 import MaintenanceTrackingLatestFeatureV1


class MaintenanceTrackingLatestFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of maintenance trackings latest values

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[MaintenanceTrackingLatestFeatureV1] = Field(alias="features")
