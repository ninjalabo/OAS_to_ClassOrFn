from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetDataV1 import WeathercamPresetDataV1


class WeathercamStationDataV1(BaseModel):
    """
    None model
        Weathercam stations&#39; data

    """

    id: str = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    presets: List[WeathercamPresetDataV1] = Field(alias="presets")
