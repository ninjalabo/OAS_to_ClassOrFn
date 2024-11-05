from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class InternationalIdentifier(BaseModel):
    """
    None model

    """

    country: str = Field(alias="country")

    nationalIdentifier: str = Field(alias="nationalIdentifier")

    get_InternationalIdentifierExtension: Optional[_ExtensionType] = Field(
        alias="get_InternationalIdentifierExtension", default=None
    )

    internationalIdentifierExtension: Optional[_ExtensionType] = Field(
        alias="internationalIdentifierExtension", default=None
    )
