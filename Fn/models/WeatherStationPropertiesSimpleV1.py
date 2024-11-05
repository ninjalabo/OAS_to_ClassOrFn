from typing import *

from pydantic import BaseModel, Field


class WeatherStationPropertiesSimpleV1(BaseModel):
    """
    None model
        Weather station properties object with basic information

    """

    id: int = Field(alias="id")

    name: Optional[str] = Field(alias="name", default=None)

    collectionStatus: Optional[str] = Field(alias="collectionStatus", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)
