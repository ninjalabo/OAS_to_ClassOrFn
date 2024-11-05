from typing import *

from pydantic import BaseModel, Field

from ._ComputationMethodEnum import _ComputationMethodEnum
from ._DirectionEnum import _DirectionEnum
from ._ExtensionType import _ExtensionType
from ._MeasuredOrDerivedDataTypeEnum import _MeasuredOrDerivedDataTypeEnum
from .AxleCharacteristics import AxleCharacteristics
from .Lane import Lane
from .VehicleCharacteristics import VehicleCharacteristics


class MeasurementSpecificCharacteristics(BaseModel):
    """
    None model

    """

    accuracy: Optional[float] = Field(alias="accuracy", default=None)

    computationMethod: Optional[_ComputationMethodEnum] = Field(alias="computationMethod", default=None)

    defaultMeasurementHeight: Optional[float] = Field(alias="defaultMeasurementHeight", default=None)

    measurementSide: Optional[_DirectionEnum] = Field(alias="measurementSide", default=None)

    period: Optional[float] = Field(alias="period", default=None)

    smoothingFactor: Optional[float] = Field(alias="smoothingFactor", default=None)

    specificMeasurementValueType: _MeasuredOrDerivedDataTypeEnum = Field(alias="specificMeasurementValueType")

    specificVehicleCharacteristics: Optional[VehicleCharacteristics] = Field(
        alias="specificVehicleCharacteristics", default=None
    )

    specificLanes: Optional[List[Optional[Lane]]] = Field(alias="specificLanes", default=None)

    axleCharacteristics: Optional[AxleCharacteristics] = Field(alias="axleCharacteristics", default=None)

    get_MeasurementSpecificCharacteristicsExtension: Optional[_ExtensionType] = Field(
        alias="get_MeasurementSpecificCharacteristicsExtension", default=None
    )
