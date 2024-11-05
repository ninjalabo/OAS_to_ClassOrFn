from typing import *

from pydantic import BaseModel, Field

from .WeatherStationDataDtoV1 import WeatherStationDataDtoV1


class WeatherStationsDataDtoV1(BaseModel):
    """
    None model
        Latest measurement data from Weather stations

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    stations: Optional[List[Optional[WeatherStationDataDtoV1]]] = Field(alias="stations", default=None)
