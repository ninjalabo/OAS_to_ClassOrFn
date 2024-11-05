from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .InternationalIdentifier import InternationalIdentifier
from .LocationReference import LocationReference
from .MultilingualString import MultilingualString
from .PhysicalQuantityFault import PhysicalQuantityFault
from .Source import Source


class PhysicalQuantity(BaseModel):
    """
    None model

    """

    forecast: Optional[bool] = Field(alias="forecast", default=None)

    measurementEquipmentTypeUsed: Optional[MultilingualString] = Field(
        alias="measurementEquipmentTypeUsed", default=None
    )

    pertinentLocation: Optional[LocationReference] = Field(alias="pertinentLocation", default=None)

    physicalQuantityFaults: Optional[List[Optional[PhysicalQuantityFault]]] = Field(
        alias="physicalQuantityFaults", default=None
    )

    source: Optional[Source] = Field(alias="source", default=None)

    informationManagerOverride: Optional[InternationalIdentifier] = Field(
        alias="informationManagerOverride", default=None
    )

    get_PhysicalQuantityExtension: Optional[_ExtensionType] = Field(alias="get_PhysicalQuantityExtension", default=None)
