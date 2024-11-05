from typing import *

from pydantic import BaseModel, Field

from .SensorValueDtoV1 import SensorValueDtoV1


class TmsStationDataDtoV1(BaseModel):
    """
    None model
        TMS station data with sensor values

    """

    id: int = Field(alias="id")

    tmsNumber: int = Field(alias="tmsNumber")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    sensorValues: List[SensorValueDtoV1] = Field(alias="sensorValues")
