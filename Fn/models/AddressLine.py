from typing import *

from pydantic import BaseModel, Field

from ._AddressLineTypeEnum import _AddressLineTypeEnum
from ._ExtensionType import _ExtensionType
from .MultilingualString import MultilingualString


class AddressLine(BaseModel):
    """
    None model

    """

    type: _AddressLineTypeEnum = Field(alias="type")

    text: MultilingualString = Field(alias="text")

    get_AddressLineExtension: Optional[_ExtensionType] = Field(alias="get_AddressLineExtension", default=None)

    order: Optional[int] = Field(alias="order", default=None)
