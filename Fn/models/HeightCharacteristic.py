from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType


class HeightCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    vehicleHeight: Optional[float] = Field(alias="vehicleHeight", default=None)

    get_HeightCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_HeightCharacteristicExtension", default=None
    )
