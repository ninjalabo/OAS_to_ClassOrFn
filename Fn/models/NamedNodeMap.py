from typing import *

from pydantic import BaseModel, Field

from .Node import Node


class NamedNodeMap(BaseModel):
    """
    None model

    """

    length: Optional[int] = Field(alias="length", default=None)

    namedItem: Optional[Node] = Field(alias="namedItem", default=None)

    namedItemNS: Optional[Node] = Field(alias="namedItemNS", default=None)
