from typing import *

from pydantic import BaseModel, Field


class SensorValueDtoV1(BaseModel):
    """
    None model
        Sensor value

    """

    id: int = Field(alias="id")

    stationId: int = Field(alias="stationId")

    name: str = Field(alias="name")

    shortName: str = Field(alias="shortName")

    timeWindowStart: Optional[str] = Field(alias="timeWindowStart", default=None)

    timeWindowEnd: Optional[str] = Field(alias="timeWindowEnd", default=None)

    measuredTime: str = Field(alias="measuredTime")

    value: float = Field(alias="value")

    reliability: Optional[str] = Field(alias="reliability", default=None)

    unit: str = Field(alias="unit")

    sensorValueDescriptionFi: Optional[str] = Field(alias="sensorValueDescriptionFi", default=None)

    sensorValueDescriptionEn: Optional[str] = Field(alias="sensorValueDescriptionEn", default=None)
