from typing import *

from pydantic import BaseModel, Field


class WeatherSensorValueHistoryDto(BaseModel):
    """
    None model

    """

    roadStationId: Optional[int] = Field(alias="roadStationId", default=None)

    sensorId: Optional[int] = Field(alias="sensorId", default=None)

    sensorValue: Optional[float] = Field(alias="sensorValue", default=None)

    measured: Optional[str] = Field(alias="measured", default=None)

    reliability: Optional[str] = Field(alias="reliability", default=None)

    measuredTime: Optional[str] = Field(alias="measuredTime", default=None)
