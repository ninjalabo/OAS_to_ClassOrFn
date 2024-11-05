from typing import *

from pydantic import BaseModel, Field


class UpdateInfoDtoV1(BaseModel):
    """
    None model
        Info about API data updates (update intervals, last updated times)

    """

    api: str = Field(alias="api")

    subtype: Optional[str] = Field(alias="subtype", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    dataCheckedTime: Optional[str] = Field(alias="dataCheckedTime", default=None)

    dataUpdateInterval: Optional[str] = Field(alias="dataUpdateInterval", default=None)

    recommendedFetchInterval: str = Field(alias="recommendedFetchInterval")
