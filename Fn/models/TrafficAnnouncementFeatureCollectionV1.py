from typing import *

from pydantic import BaseModel, Field

from .TrafficAnnouncementFeatureV1 import TrafficAnnouncementFeatureV1


class TrafficAnnouncementFeatureCollectionV1(BaseModel):
    """
    None model
        GeoJSON Feature Collection of Traffic Announcements

    """

    type: str = Field(alias="type")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    features: List[TrafficAnnouncementFeatureV1] = Field(alias="features")
