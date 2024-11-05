from typing import *

from pydantic import BaseModel, Field

from .UpdateInfoDtoV1 import UpdateInfoDtoV1


class UpdateInfosDtoV1(BaseModel):
    """
    None model
        Info about API data updates (update intervals, last updated times)

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    updateTimes: Optional[List[Optional[UpdateInfoDtoV1]]] = Field(alias="updateTimes", default=None)
