from typing import *

from pydantic import BaseModel, Field


class SensorValueDescription(BaseModel):
    """
    None model
        Additional information of sensor values

    """

    descriptionEn: Optional[str] = Field(alias="descriptionEn", default=None)

    descriptionFi: Optional[str] = Field(alias="descriptionFi", default=None)

    sensorValue: Optional[float] = Field(alias="sensorValue", default=None)
