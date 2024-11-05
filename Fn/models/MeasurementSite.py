from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._MeasurementSiteIndexMeasurementSpecificCharacteristics import \
    _MeasurementSiteIndexMeasurementSpecificCharacteristics
from .InternationalIdentifier import InternationalIdentifier
from .LocationReference import LocationReference
from .MultilingualString import MultilingualString


class MeasurementSite(BaseModel):
    """
    None model

    """

    measurementSiteRecordVersionTime: Optional[str] = Field(alias="measurementSiteRecordVersionTime", default=None)

    measurementEquipmentReference: Optional[str] = Field(alias="measurementEquipmentReference", default=None)

    measurementEquipmentTypeUsed: Optional[MultilingualString] = Field(
        alias="measurementEquipmentTypeUsed", default=None
    )

    measurementSiteName: Optional[MultilingualString] = Field(alias="measurementSiteName", default=None)

    measurementSiteNumberOfLanes: Optional[int] = Field(alias="measurementSiteNumberOfLanes", default=None)

    measurementSiteIdentification: Optional[str] = Field(alias="measurementSiteIdentification", default=None)

    measurementSpecificCharacteristics: Optional[
        List[Optional[_MeasurementSiteIndexMeasurementSpecificCharacteristics]]
    ] = Field(alias="measurementSpecificCharacteristics", default=None)

    measurementSiteLocation: LocationReference = Field(alias="measurementSiteLocation")

    informationManagerOverride: Optional[InternationalIdentifier] = Field(
        alias="informationManagerOverride", default=None
    )

    get_MeasurementSiteExtension: Optional[_ExtensionType] = Field(alias="get_MeasurementSiteExtension", default=None)

    id: Optional[str] = Field(alias="id", default=None)

    version: Optional[str] = Field(alias="version", default=None)
