from typing import *

from pydantic import BaseModel, Field


class NodeList(BaseModel):
    """
    None model

    """

    length: Optional[int] = Field(alias="length", default=None)
