from typing import *

from pydantic import BaseModel, Field

from ._LocationReferenceExtensionType import _LocationReferenceExtensionType


class LocationReference(BaseModel):
    """
    None model

    """

    get_LocationReferenceExtension: Optional[_LocationReferenceExtensionType] = Field(
        alias="get_LocationReferenceExtension", default=None
    )
