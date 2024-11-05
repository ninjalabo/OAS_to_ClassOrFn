from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetHistoryDtoV1 import WeathercamPresetHistoryDtoV1


class PresetHistory(BaseModel):
    """
    None model
        Weather camera preset&#39;s image history.

    """

    id: str = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    presets: List[WeathercamPresetHistoryDtoV1] = Field(alias="presets")
