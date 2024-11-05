from typing import *

from pydantic import BaseModel, Field

from .SensorValueDtoV1 import SensorValueDtoV1


class WeatherStationDataDtoV1(BaseModel):
    """
    None model
        Weather station data with sensor values

    """

    id: int = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    sensorValues: List[SensorValueDtoV1] = Field(alias="sensorValues")
