from typing import *

from pydantic import BaseModel, Field


class CounterModel(BaseModel):
    """
    None model
        Counting Site Metadata

    """

    domain: Optional[str] = Field(alias="domain", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    interval: Optional[int] = Field(alias="interval", default=None)

    lastDataTimestamp: Optional[str] = Field(alias="lastDataTimestamp", default=None)

    removedTimestamp: Optional[str] = Field(alias="removedTimestamp", default=None)

    id: Optional[int] = Field(alias="id", default=None)

    userType: Optional[int] = Field(alias="userType", default=None)

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    direction: Optional[int] = Field(alias="direction", default=None)
