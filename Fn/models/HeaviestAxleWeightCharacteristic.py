from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType


class HeaviestAxleWeightCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    heaviestAxleWeight: Optional[float] = Field(alias="heaviestAxleWeight", default=None)

    get_HeaviestAxleWeightCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_HeaviestAxleWeightCharacteristicExtension", default=None
    )
