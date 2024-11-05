from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType


class WidthCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    vehicleWidth: Optional[float] = Field(alias="vehicleWidth", default=None)

    get_WidthCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_WidthCharacteristicExtension", default=None
    )
