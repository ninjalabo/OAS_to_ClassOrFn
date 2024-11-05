from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._PublicEventTypeEnum import _PublicEventTypeEnum
from ._SpecialDayTypeEnum import _SpecialDayTypeEnum
from .NamedArea import NamedArea


class SpecialDay(BaseModel):
    """
    None model

    """

    intersectWithApplicableDays: Optional[bool] = Field(alias="intersectWithApplicableDays", default=None)

    specialDayType: _SpecialDayTypeEnum = Field(alias="specialDayType")

    publicEvent: Optional[_PublicEventTypeEnum] = Field(alias="publicEvent", default=None)

    namedAreas: Optional[List[Optional[NamedArea]]] = Field(alias="namedAreas", default=None)

    get_SpecialDayExtension: Optional[_ExtensionType] = Field(alias="get_SpecialDayExtension", default=None)
