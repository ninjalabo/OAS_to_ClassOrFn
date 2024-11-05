from typing import *

from pydantic import BaseModel, Field

from .WeathercamStationDataV1 import WeathercamStationDataV1


class WeathercamStationsDataV1(BaseModel):
    """
    None model
        Weathercam stations&#39; data

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    stations: Optional[List[Optional[WeathercamStationDataV1]]] = Field(alias="stations", default=None)
