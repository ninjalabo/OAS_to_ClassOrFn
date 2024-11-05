from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetPublicityHistoryV1 import WeathercamPresetPublicityHistoryV1


class WeathercamStationPresetsPublicityHistoryV1(BaseModel):
    """
    None model
        Weathercam station presets publicity changes

    """

    id: str = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    presets: List[WeathercamPresetPublicityHistoryV1] = Field(alias="presets")
