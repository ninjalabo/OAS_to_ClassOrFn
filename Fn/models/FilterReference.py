from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class FilterReference(BaseModel):
    """
    None model

    """

    deleteFilter: Optional[bool] = Field(alias="deleteFilter", default=None)

    filterOperationApproved: Optional[bool] = Field(alias="filterOperationApproved", default=None)

    keyFilterReference: str = Field(alias="keyFilterReference")

    filterReferenceExtension: Optional[_ExtensionType] = Field(alias="filterReferenceExtension", default=None)
