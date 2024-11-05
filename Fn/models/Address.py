from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .AddressLine import AddressLine
from .MultilingualString import MultilingualString


class Address(BaseModel):
    """
    None model

    """

    postcode: Optional[str] = Field(alias="postcode", default=None)

    city: Optional[MultilingualString] = Field(alias="city", default=None)

    countryCode: Optional[str] = Field(alias="countryCode", default=None)

    addressLines: Optional[List[Optional[AddressLine]]] = Field(alias="addressLines", default=None)

    get_AddressExtension: Optional[_ExtensionType] = Field(alias="get_AddressExtension", default=None)
