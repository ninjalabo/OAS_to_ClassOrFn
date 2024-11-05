from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class Target(BaseModel):
    """
    None model

    """

    address: str = Field(alias="address")

    protocol: str = Field(alias="protocol")

    targetExtension: Optional[_ExtensionType] = Field(alias="targetExtension", default=None)
