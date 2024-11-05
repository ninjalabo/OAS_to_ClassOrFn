from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .InternationalIdentifier import InternationalIdentifier
from .MeasurementSite import MeasurementSite


class MeasurementSiteTable(BaseModel):
    """
    None model

    """

    measurementSiteTableIdentification: Optional[str] = Field(alias="measurementSiteTableIdentification", default=None)

    measurementSites: List[MeasurementSite] = Field(alias="measurementSites")

    informationManager: Optional[InternationalIdentifier] = Field(alias="informationManager", default=None)

    get_MeasurementSiteTableExtension: Optional[_ExtensionType] = Field(
        alias="get_MeasurementSiteTableExtension", default=None
    )

    id: Optional[str] = Field(alias="id", default=None)

    version: Optional[str] = Field(alias="version", default=None)
