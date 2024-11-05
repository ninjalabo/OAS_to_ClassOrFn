from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._PhysicalQuantityFaultEnum import _PhysicalQuantityFaultEnum


class PhysicalQuantityFault(BaseModel):
    """
    None model

    """

    faultLastUpdateTime: str = Field(alias="faultLastUpdateTime")

    get_FaultExtension: Optional[_ExtensionType] = Field(alias="get_FaultExtension", default=None)

    physicalQuantityFaultType: _PhysicalQuantityFaultEnum = Field(alias="physicalQuantityFaultType")

    get_PhysicalQuantityFaultExtension: Optional[_ExtensionType] = Field(
        alias="get_PhysicalQuantityFaultExtension", default=None
    )
