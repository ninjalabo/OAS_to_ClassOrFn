from typing import *

from pydantic import BaseModel, Field

from ._DayEnum import _DayEnum
from ._ExtensionType import _ExtensionType
from ._MonthOfYearEnum import _MonthOfYearEnum


class DayWeekMonth(BaseModel):
    """
    None model

    """

    applicableDaies: Optional[List[Optional[_DayEnum]]] = Field(alias="applicableDaies", default=None)

    applicableMonths: Optional[List[Optional[_MonthOfYearEnum]]] = Field(alias="applicableMonths", default=None)

    get_DayWeekMonthExtension: Optional[_ExtensionType] = Field(alias="get_DayWeekMonthExtension", default=None)
