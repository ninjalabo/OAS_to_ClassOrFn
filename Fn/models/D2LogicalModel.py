from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .Exchange import Exchange
from .PayloadPublication import PayloadPublication


class D2LogicalModel(BaseModel):
    """
    None model

    """

    exchange: Exchange = Field(alias="exchange")

    payloadPublication: Optional[PayloadPublication] = Field(alias="payloadPublication", default=None)

    d2LogicalModelExtension: Optional[_ExtensionType] = Field(alias="d2LogicalModelExtension", default=None)
