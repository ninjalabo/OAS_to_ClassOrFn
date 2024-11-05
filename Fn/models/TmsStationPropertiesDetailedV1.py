from typing import *

from pydantic import BaseModel, Field

from .StationRoadAddressV1 import StationRoadAddressV1


class TmsStationPropertiesDetailedV1(BaseModel):
    """
    None model
        Tms station properties object with basic information

    """

    id: int = Field(alias="id")

    tmsNumber: int = Field(alias="tmsNumber")

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

    direction1Municipality: str = Field(alias="direction1Municipality")

    direction1MunicipalityCode: Optional[int] = Field(alias="direction1MunicipalityCode", default=None)

    direction2Municipality: str = Field(alias="direction2Municipality")

    direction2MunicipalityCode: Optional[int] = Field(alias="direction2MunicipalityCode", default=None)

    stationType: Optional[str] = Field(alias="stationType", default=None)

    calculatorDeviceType: Optional[str] = Field(alias="calculatorDeviceType", default=None)

    sensors: Optional[List[int]] = Field(alias="sensors", default=None)

    freeFlowSpeed1: Optional[float] = Field(alias="freeFlowSpeed1", default=None)

    freeFlowSpeed2: Optional[float] = Field(alias="freeFlowSpeed2", default=None)
