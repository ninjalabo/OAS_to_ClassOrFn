from typing import *

from pydantic import BaseModel, Field


class SignTextRowV1(BaseModel):
    """
    None model
        Variable Sign text row

    """

    screen: Optional[int] = Field(alias="screen", default=None)

    rowNumber: Optional[int] = Field(alias="rowNumber", default=None)

    text: Optional[str] = Field(alias="text", default=None)
