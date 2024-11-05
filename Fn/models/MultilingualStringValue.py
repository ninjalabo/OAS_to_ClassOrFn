from typing import *

from pydantic import BaseModel, Field


class MultilingualStringValue(BaseModel):
    """
    None model

    """

    value: Optional[str] = Field(alias="value", default=None)

    lang: Optional[str] = Field(alias="lang", default=None)
