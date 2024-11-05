from typing import *

from pydantic import BaseModel, Field

from .TmsStationSensorDtoV1 import TmsStationSensorDtoV1


class TmsStationSensorsDtoV1(BaseModel):
    """
    None model
        Available sensors of TMS stations

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    dataLastCheckedTime: str = Field(alias="dataLastCheckedTime")

    sensors: List[TmsStationSensorDtoV1] = Field(alias="sensors")
