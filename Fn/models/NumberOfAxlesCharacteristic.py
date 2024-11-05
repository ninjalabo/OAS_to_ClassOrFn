from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType


class NumberOfAxlesCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    numberOfAxles: int = Field(alias="numberOfAxles")

    get_NumberOfAxlesCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_NumberOfAxlesCharacteristicExtension", default=None
    )
