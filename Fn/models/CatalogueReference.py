from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class CatalogueReference(BaseModel):
    """
    None model

    """

    keyCatalogueReference: str = Field(alias="keyCatalogueReference")

    catalogueReferenceExtension: Optional[_ExtensionType] = Field(alias="catalogueReferenceExtension", default=None)
