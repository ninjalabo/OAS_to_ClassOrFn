from typing import *

from pydantic import BaseModel, Field

from .Element import Element
from .EmissionsExtension import EmissionsExtension


class _EmissionsExtensionType(BaseModel):
    """
    None model

    """

    emissionsExtension: Optional[EmissionsExtension] = Field(alias="emissionsExtension", default=None)

    anies: Optional[List[Optional[Element]]] = Field(alias="anies", default=None)
