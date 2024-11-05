from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._FuelTypeEnum import _FuelTypeEnum
from ._LoadTypeEnum import _LoadTypeEnum
from ._VehicleEquipmentEnum import _VehicleEquipmentEnum
from ._VehicleTypeEnum import _VehicleTypeEnum
from ._VehicleUsageEnum import _VehicleUsageEnum
from .Emissions import Emissions
from .GrossWeightCharacteristic import GrossWeightCharacteristic
from .HeaviestAxleWeightCharacteristic import HeaviestAxleWeightCharacteristic
from .HeightCharacteristic import HeightCharacteristic
from .LengthCharacteristic import LengthCharacteristic
from .NumberOfAxlesCharacteristic import NumberOfAxlesCharacteristic
from .WidthCharacteristic import WidthCharacteristic


class VehicleCharacteristics(BaseModel):
    """
    None model

    """

    fuelTypes: Optional[List[Optional[_FuelTypeEnum]]] = Field(alias="fuelTypes", default=None)

    loadType: Optional[_LoadTypeEnum] = Field(alias="loadType", default=None)

    vehicleEquipment: Optional[_VehicleEquipmentEnum] = Field(alias="vehicleEquipment", default=None)

    vehicleTypes: Optional[List[Optional[_VehicleTypeEnum]]] = Field(alias="vehicleTypes", default=None)

    vehicleUsage: Optional[_VehicleUsageEnum] = Field(alias="vehicleUsage", default=None)

    yearOfFirstRegistration: Optional[int] = Field(alias="yearOfFirstRegistration", default=None)

    grossWeightCharacteristics: Optional[List[Optional[GrossWeightCharacteristic]]] = Field(
        alias="grossWeightCharacteristics", default=None
    )

    heightCharacteristics: Optional[List[Optional[HeightCharacteristic]]] = Field(
        alias="heightCharacteristics", default=None
    )

    lengthCharacteristics: Optional[List[Optional[LengthCharacteristic]]] = Field(
        alias="lengthCharacteristics", default=None
    )

    widthCharacteristics: Optional[List[Optional[WidthCharacteristic]]] = Field(
        alias="widthCharacteristics", default=None
    )

    heaviestAxleWeightCharacteristics: Optional[List[Optional[HeaviestAxleWeightCharacteristic]]] = Field(
        alias="heaviestAxleWeightCharacteristics", default=None
    )

    numberOfAxlesCharacteristics: Optional[List[Optional[NumberOfAxlesCharacteristic]]] = Field(
        alias="numberOfAxlesCharacteristics", default=None
    )

    emissions: Optional[Emissions] = Field(alias="emissions", default=None)

    get_VehicleCharacteristicsExtension: Optional[_ExtensionType] = Field(
        alias="get_VehicleCharacteristicsExtension", default=None
    )
