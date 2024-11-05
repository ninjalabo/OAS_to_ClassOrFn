from typing import *

from pydantic import BaseModel, Field

from .HistoryTextRowV1 import HistoryTextRowV1


class TrafficSignHistoryV1(BaseModel):
    """
    None model

    """

    cause: Optional[str] = Field(alias="cause", default=None)

    rows: Optional[List[Optional[HistoryTextRowV1]]] = Field(alias="rows", default=None)

    displayValue: Optional[str] = Field(alias="displayValue", default=None)

    additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None)

    effectDate: Optional[str] = Field(alias="effectDate", default=None)
