from typing import *

from pydantic import BaseModel, Field

from ._ConfidentialityValueEnum import _ConfidentialityValueEnum
from ._ExtensionType import _ExtensionType
from ._InformationDeliveryServicesEnum import _InformationDeliveryServicesEnum
from ._InformationStatusEnum import _InformationStatusEnum


class HeaderInformation(BaseModel):
    """
    None model

    """

    confidentiality: Optional[_ConfidentialityValueEnum] = Field(alias="confidentiality", default=None)

    allowedDeliveryChannels: Optional[List[Optional[_InformationDeliveryServicesEnum]]] = Field(
        alias="allowedDeliveryChannels", default=None
    )

    informationStatus: _InformationStatusEnum = Field(alias="informationStatus")

    get_HeaderInformationExtension: Optional[_ExtensionType] = Field(
        alias="get_HeaderInformationExtension", default=None
    )
