from typing import *

from pydantic import BaseModel, Field

from .StationRoadAddressV1 import StationRoadAddressV1


class WeatherStationPropertiesDetailedV1(BaseModel):
    """
    None model
        Weather station properties object with basic information

    """

    id: int = Field(alias="id")

    name: Optional[str] = Field(alias="name", default=None)

    collectionStatus: Optional[str] = Field(alias="collectionStatus", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    collectionInterval: Optional[int] = Field(alias="collectionInterval", default=None)

    names: Optional[Dict[str, Any]] = Field(alias="names", default=None)

    roadAddress: Optional[StationRoadAddressV1] = Field(alias="roadAddress", default=None)

    liviId: Optional[str] = Field(alias="liviId", default=None)

    country: Optional[str] = Field(alias="country", default=None)

    startTime: Optional[str] = Field(alias="startTime", default=None)

    repairMaintenanceTime: Optional[str] = Field(alias="repairMaintenanceTime", default=None)

    annualMaintenanceTime: Optional[str] = Field(alias="annualMaintenanceTime", default=None)

    purpose: Optional[str] = Field(alias="purpose", default=None)

    municipality: Optional[str] = Field(alias="municipality", default=None)

    municipalityCode: Optional[int] = Field(alias="municipalityCode", default=None)

    province: Optional[str] = Field(alias="province", default=None)

    provinceCode: Optional[int] = Field(alias="provinceCode", default=None)

    stationType: Optional[str] = Field(alias="stationType", default=None)

    master: bool = Field(alias="master")

    sensors: Optional[List[int]] = Field(alias="sensors", default=None)
