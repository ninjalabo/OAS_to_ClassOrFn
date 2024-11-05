from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType


class LengthCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    vehicleLength: Optional[float] = Field(alias="vehicleLength", default=None)

    get_LengthCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_LengthCharacteristicExtension", default=None
    )
