from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .CatalogueReference import CatalogueReference
from .FilterReference import FilterReference
from .InternationalIdentifier import InternationalIdentifier
from .Subscription import Subscription
from .Target import Target


class Exchange(BaseModel):
    """
    None model

    """

    changedFlag: Optional[str] = Field(alias="changedFlag", default=None)

    clientIdentification: Optional[str] = Field(alias="clientIdentification", default=None)

    deliveryBreak: Optional[bool] = Field(alias="deliveryBreak", default=None)

    denyReason: Optional[str] = Field(alias="denyReason", default=None)

    historicalStartDate: Optional[str] = Field(alias="historicalStartDate", default=None)

    historicalStopDate: Optional[str] = Field(alias="historicalStopDate", default=None)

    keepAlive: Optional[bool] = Field(alias="keepAlive", default=None)

    requestType: Optional[str] = Field(alias="requestType", default=None)

    response: Optional[str] = Field(alias="response", default=None)

    subscriptionReference: Optional[str] = Field(alias="subscriptionReference", default=None)

    supplierIdentification: InternationalIdentifier = Field(alias="supplierIdentification")

    target: Optional[Target] = Field(alias="target", default=None)

    subscription: Optional[Subscription] = Field(alias="subscription", default=None)

    filterReferences: Optional[List[Optional[FilterReference]]] = Field(alias="filterReferences", default=None)

    catalogueReferences: Optional[List[Optional[CatalogueReference]]] = Field(alias="catalogueReferences", default=None)

    exchangeExtension: Optional[_ExtensionType] = Field(alias="exchangeExtension", default=None)
