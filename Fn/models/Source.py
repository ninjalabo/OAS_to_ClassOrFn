from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._SourceTypeEnum import _SourceTypeEnum
from .MultilingualString import MultilingualString


class Source(BaseModel):
    """
    None model

    """

    sourceCountry: Optional[str] = Field(alias="sourceCountry", default=None)

    sourceIdentification: Optional[str] = Field(alias="sourceIdentification", default=None)

    sourceName: Optional[MultilingualString] = Field(alias="sourceName", default=None)

    sourceType: Optional[_SourceTypeEnum] = Field(alias="sourceType", default=None)

    reliable: Optional[bool] = Field(alias="reliable", default=None)

    get_SourceExtension: Optional[_ExtensionType] = Field(alias="get_SourceExtension", default=None)
