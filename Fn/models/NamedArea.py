from typing import *

from pydantic import BaseModel, Field

from .ExtensionTypeG import ExtensionTypeG
from .MultilingualString import MultilingualString
from .NamedAreaTypeEnumG import NamedAreaTypeEnumG


class NamedArea(BaseModel):
    """
    None model

    """

    areaName: MultilingualString = Field(alias="areaName")

    namedAreaType: Optional[NamedAreaTypeEnumG] = Field(alias="namedAreaType", default=None)

    country: Optional[str] = Field(alias="country", default=None)

    namedAreaExtensionG: Optional[ExtensionTypeG] = Field(alias="namedAreaExtensionG", default=None)
