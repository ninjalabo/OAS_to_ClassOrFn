from typing import *

from pydantic import BaseModel, Field

from .Element import Element


class _ExtensionType(BaseModel):
    """
    None model

    """

    anies: Optional[List[Optional[Element]]] = Field(alias="anies", default=None)
