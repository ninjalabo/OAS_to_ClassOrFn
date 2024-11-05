from typing import *

from pydantic import BaseModel, Field

from .LocationDetailsV1 import LocationDetailsV1
from .LocationV1 import LocationV1
from .RestrictionV1 import RestrictionV1
from .TimeAndDurationV1 import TimeAndDurationV1
from .WeekdayTimePeriodV1 import WeekdayTimePeriodV1
from .WorkTypeV1 import WorkTypeV1


class RoadWorkPhaseV1(BaseModel):
    """
    None model
        A single phase in a larger road work

    """

    id: str = Field(alias="id")

    location: Optional[LocationV1] = Field(alias="location", default=None)

    locationDetails: Optional[LocationDetailsV1] = Field(alias="locationDetails", default=None)

    workingHours: List[WeekdayTimePeriodV1] = Field(alias="workingHours")

    comment: Optional[str] = Field(alias="comment", default=None)

    timeAndDuration: TimeAndDurationV1 = Field(alias="timeAndDuration")

    workTypes: Optional[List[Optional[WorkTypeV1]]] = Field(alias="workTypes", default=None)

    restrictions: Optional[List[Optional[RestrictionV1]]] = Field(alias="restrictions", default=None)

    restrictionsLiftable: Optional[bool] = Field(alias="restrictionsLiftable", default=None)

    severity: str = Field(alias="severity")

    slowTrafficTimes: Optional[List[Optional[WeekdayTimePeriodV1]]] = Field(alias="slowTrafficTimes", default=None)

    queuingTrafficTimes: Optional[List[Optional[WeekdayTimePeriodV1]]] = Field(
        alias="queuingTrafficTimes", default=None
    )
