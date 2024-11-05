from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetHistoryItemDtoV1 import WeathercamPresetHistoryItemDtoV1


class WeathercamPresetHistoryDtoV1(BaseModel):
    """
    None model
        Weather camera preset&#39;s image history.

    """

    id: str = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    history: List[WeathercamPresetHistoryItemDtoV1] = Field(alias="history")
