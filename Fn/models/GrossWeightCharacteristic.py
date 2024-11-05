from typing import *

from pydantic import BaseModel, Field

from ._ComparisonOperatorEnum import _ComparisonOperatorEnum
from ._ExtensionType import _ExtensionType
from ._WeightTypeEnum import _WeightTypeEnum


class GrossWeightCharacteristic(BaseModel):
    """
    None model

    """

    comparisonOperator: _ComparisonOperatorEnum = Field(alias="comparisonOperator")

    grossVehicleWeight: Optional[float] = Field(alias="grossVehicleWeight", default=None)

    typeOfWeight: _WeightTypeEnum = Field(alias="typeOfWeight")

    get_GrossWeightCharacteristicExtension: Optional[_ExtensionType] = Field(
        alias="get_GrossWeightCharacteristicExtension", default=None
    )
