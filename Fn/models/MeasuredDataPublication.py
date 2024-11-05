from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._MeasurementSiteTableVersionedReference import _MeasurementSiteTableVersionedReference
from .HeaderInformation import HeaderInformation
from .InternationalIdentifier import InternationalIdentifier
from .SiteMeasurements import SiteMeasurements


class MeasuredDataPublication(BaseModel):
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

    measurementSiteTableReferences: List[_MeasurementSiteTableVersionedReference] = Field(
        alias="measurementSiteTableReferences"
    )

    headerInformation: HeaderInformation = Field(alias="headerInformation")

    siteMeasurements: List[SiteMeasurements] = Field(alias="siteMeasurements")

    get_MeasuredDataPublicationExtension: Optional[_ExtensionType] = Field(
        alias="get_MeasuredDataPublicationExtension", default=None
    )
