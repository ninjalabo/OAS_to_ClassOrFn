from typing import *

from pydantic import BaseModel, Field

from .WeatherStationSensorDtoV1 import WeatherStationSensorDtoV1


class WeatherStationSensorsDtoV1(BaseModel):
    """
    None model
        Available sensors of weather stations

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    dataLastCheckedTime: str = Field(alias="dataLastCheckedTime")

    sensors: List[WeatherStationSensorDtoV1] = Field(alias="sensors")
