from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class TimePeriodOfDay(BaseModel):
    """
    None model

    """

    startTimeOfPeriod: str = Field(alias="startTimeOfPeriod")

    endTimeOfPeriod: str = Field(alias="endTimeOfPeriod")

    get_TimePeriodOfDayExtension: Optional[_ExtensionType] = Field(alias="get_TimePeriodOfDayExtension", default=None)
