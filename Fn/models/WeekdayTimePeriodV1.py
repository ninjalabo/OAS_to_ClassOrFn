from typing import *

from pydantic import BaseModel, Field

from .LocalTime import LocalTime


class WeekdayTimePeriodV1(BaseModel):
    """
    None model
        Weekday time period

    """

    weekday: str = Field(alias="weekday")

    startTime: LocalTime = Field(alias="startTime")

    endTime: LocalTime = Field(alias="endTime")
