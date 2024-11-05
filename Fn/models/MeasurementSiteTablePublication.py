from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .HeaderInformation import HeaderInformation
from .InternationalIdentifier import InternationalIdentifier
from .MeasurementSiteTable import MeasurementSiteTable


class MeasurementSiteTablePublication(BaseModel):
    """
    None model

    """

    publicationTime: str = Field(alias="publicationTime")

    publicationCreator: InternationalIdentifier = Field(alias="publicationCreator")

    get_PayloadPublicationExtension: Optional[_ExtensionType] = Field(
        alias="get_PayloadPublicationExtension", default=None
    )

    lang: Optional[str] = Field(alias="lang", default=None)

    extensionName: Optional[str] = Field(alias="extensionName", default=None)

    extensionVersion: Optional[str] = Field(alias="extensionVersion", default=None)

    profileName: Optional[str] = Field(alias="profileName", default=None)

    profileVersion: Optional[str] = Field(alias="profileVersion", default=None)

    headerInformation: HeaderInformation = Field(alias="headerInformation")

    measurementSiteTables: List[MeasurementSiteTable] = Field(alias="measurementSiteTables")

    get_MeasurementSiteTablePublicationExtension: Optional[_ExtensionType] = Field(
        alias="get_MeasurementSiteTablePublicationExtension", default=None
    )
