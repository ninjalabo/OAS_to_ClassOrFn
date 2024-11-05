from typing import *

from pydantic import BaseModel, Field

from .TmsSensorConstantValueDtoV1 import TmsSensorConstantValueDtoV1


class TmsStationSensorConstantDtoV1(BaseModel):
    """
    None model
        Sensor constant of TMS Station

    """

    id: int = Field(alias="id")

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    sensorConstantValues: List[TmsSensorConstantValueDtoV1] = Field(alias="sensorConstantValues")
