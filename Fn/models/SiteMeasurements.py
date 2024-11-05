from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._MeasurementSiteVersionedReference import _MeasurementSiteVersionedReference
from ._SiteMeasurementsIndexPhysicalQuantity import _SiteMeasurementsIndexPhysicalQuantity
from .MeasurementOrCalculationTime import MeasurementOrCalculationTime


class SiteMeasurements(BaseModel):
    """
    None model

    """

    measurementSiteReference: _MeasurementSiteVersionedReference = Field(alias="measurementSiteReference")

    physicalQuantities: Optional[List[Optional[_SiteMeasurementsIndexPhysicalQuantity]]] = Field(
        alias="physicalQuantities", default=None
    )

    measurementTimeDefault: MeasurementOrCalculationTime = Field(alias="measurementTimeDefault")

    get_SiteMeasurementsExtension: Optional[_ExtensionType] = Field(alias="get_SiteMeasurementsExtension", default=None)
