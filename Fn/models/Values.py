from typing import *

from pydantic import BaseModel, Field

from .MultilingualStringValue import MultilingualStringValue


class Values(BaseModel):
    """
    None model

    """

    values: List[MultilingualStringValue] = Field(alias="values")
