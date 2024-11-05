from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .InternationalIdentifier import InternationalIdentifier
from .MultilingualString import MultilingualString


class PayloadPublication(BaseModel):
    """
    None model

    """

    feedDescription: Optional[MultilingualString] = Field(alias="feedDescription", default=None)

    feedType: Optional[str] = Field(alias="feedType", default=None)

    publicationTime: str = Field(alias="publicationTime")

    publicationCreator: InternationalIdentifier = Field(alias="publicationCreator")

    payloadPublicationExtension: Optional[_ExtensionType] = Field(alias="payloadPublicationExtension", default=None)

    lang: Optional[str] = Field(alias="lang", default=None)
