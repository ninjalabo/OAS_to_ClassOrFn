from typing import *

from pydantic import BaseModel, Field

from .TmsStationDataDtoV1 import TmsStationDataDtoV1


class TmsStationsDataDtoV1(BaseModel):
    """
    None model
        Latest measurement data from TMS stations

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    stations: Optional[List[Optional[TmsStationDataDtoV1]]] = Field(alias="stations", default=None)
