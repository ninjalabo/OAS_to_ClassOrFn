from typing import *

from pydantic import BaseModel, Field

from .FeatureV1 import FeatureV1
from .LastActiveItinerarySegmentV1 import LastActiveItinerarySegmentV1
from .LocationDetailsV1 import LocationDetailsV1
from .LocationV1 import LocationV1
from .RoadWorkPhaseV1 import RoadWorkPhaseV1
from .TimeAndDurationV1 import TimeAndDurationV1


class TrafficAnnouncementV1(BaseModel):
    """
    None model
        Announcement time and duration

    """

    language: str = Field(alias="language")

    title: str = Field(alias="title")

    location: Optional[LocationV1] = Field(alias="location", default=None)

    locationDetails: Optional[LocationDetailsV1] = Field(alias="locationDetails", default=None)

    features: Optional[List[Optional[FeatureV1]]] = Field(alias="features", default=None)

    roadWorkPhases: Optional[List[Optional[RoadWorkPhaseV1]]] = Field(alias="roadWorkPhases", default=None)

    earlyClosing: Optional[str] = Field(alias="earlyClosing", default=None)

    comment: Optional[str] = Field(alias="comment", default=None)

    timeAndDuration: Optional[TimeAndDurationV1] = Field(alias="timeAndDuration", default=None)

    additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None)

    sender: str = Field(alias="sender")

    lastActiveItinerarySegment: Optional[LastActiveItinerarySegmentV1] = Field(
        alias="lastActiveItinerarySegment", default=None
    )
