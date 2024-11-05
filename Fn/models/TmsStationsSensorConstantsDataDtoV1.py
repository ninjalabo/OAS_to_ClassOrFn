from typing import *

from pydantic import BaseModel, Field

from .TmsStationSensorConstantDtoV1 import TmsStationSensorConstantDtoV1


class TmsStationsSensorConstantsDataDtoV1(BaseModel):
    """
    None model
        Latest sensor constant values of TMS stations

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    stations: Optional[List[Optional[TmsStationSensorConstantDtoV1]]] = Field(alias="stations", default=None)
