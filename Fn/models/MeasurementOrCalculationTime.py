from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._TimeMeaningEnum import _TimeMeaningEnum
from .Period import Period


class MeasurementOrCalculationTime(BaseModel):
    """
    None model

    """

    timeMeaning: Optional[_TimeMeaningEnum] = Field(alias="timeMeaning", default=None)

    timeValue: Optional[str] = Field(alias="timeValue", default=None)

    period: Optional[Period] = Field(alias="period", default=None)

    get_MeasurementOrCalculationTimeExtension: Optional[_ExtensionType] = Field(
        alias="get_MeasurementOrCalculationTimeExtension", default=None
    )

    timePrecision: Optional[str] = Field(alias="timePrecision", default=None)
