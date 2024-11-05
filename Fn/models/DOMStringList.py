from typing import *

from pydantic import BaseModel, Field


class DOMStringList(BaseModel):
    """
    None model

    """

    length: Optional[int] = Field(alias="length", default=None)
