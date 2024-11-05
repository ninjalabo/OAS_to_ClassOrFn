from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .DayWeekMonth import DayWeekMonth
from .MultilingualString import MultilingualString
from .SpecialDay import SpecialDay
from .TimePeriodOfDay import TimePeriodOfDay


class Period(BaseModel):
    """
    None model

    """

    startOfPeriod: Optional[str] = Field(alias="startOfPeriod", default=None)

    endOfPeriod: Optional[str] = Field(alias="endOfPeriod", default=None)

    periodName: Optional[MultilingualString] = Field(alias="periodName", default=None)

    recurringTimePeriodOfDaies: Optional[List[Optional[TimePeriodOfDay]]] = Field(
        alias="recurringTimePeriodOfDaies", default=None
    )

    recurringDayWeekMonthPeriods: Optional[List[Optional[DayWeekMonth]]] = Field(
        alias="recurringDayWeekMonthPeriods", default=None
    )

    recurringSpecialDaies: Optional[List[Optional[SpecialDay]]] = Field(alias="recurringSpecialDaies", default=None)

    get_PeriodExtension: Optional[_ExtensionType] = Field(alias="get_PeriodExtension", default=None)
