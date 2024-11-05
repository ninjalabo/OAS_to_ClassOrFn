from typing import *

from pydantic import BaseModel, Field

from .WeathercamStationPresetsPublicityHistoryV1 import WeathercamStationPresetsPublicityHistoryV1


class WeathercamStationsPresetsPublicityHistoryV1(BaseModel):
    """
    None model
        Weathercam stations presets publicity changes

    """

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    stations: Optional[List[Optional[WeathercamStationPresetsPublicityHistoryV1]]] = Field(
        alias="stations", default=None
    )
