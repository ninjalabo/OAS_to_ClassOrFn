from typing import *

from pydantic import BaseModel, Field

from .EstimatedDurationV1 import EstimatedDurationV1


class TimeAndDurationV1(BaseModel):
    """
    None model
        Announcement time and duration

    """

    startTime: str = Field(alias="startTime")

    endTime: Optional[str] = Field(alias="endTime", default=None)

    estimatedDuration: Optional[EstimatedDurationV1] = Field(alias="estimatedDuration", default=None)
