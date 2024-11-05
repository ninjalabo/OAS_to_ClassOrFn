from typing import *

from pydantic import BaseModel, Field


class HistoryTextRowV1(BaseModel):
    """
    None model

    """

    text: Optional[str] = Field(alias="text", default=None)

    screen: Optional[int] = Field(alias="screen", default=None)

    rowNumber: Optional[int] = Field(alias="rowNumber", default=None)
