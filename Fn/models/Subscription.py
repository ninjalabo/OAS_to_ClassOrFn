from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from .CatalogueReference import CatalogueReference
from .FilterReference import FilterReference
from .Target import Target


class Subscription(BaseModel):
    """
    None model

    """

    deleteSubscription: Optional[bool] = Field(alias="deleteSubscription", default=None)

    deliveryInterval: Optional[float] = Field(alias="deliveryInterval", default=None)

    operatingMode: str = Field(alias="operatingMode")

    subscriptionStartTime: str = Field(alias="subscriptionStartTime")

    subscriptionState: str = Field(alias="subscriptionState")

    subscriptionStopTime: Optional[str] = Field(alias="subscriptionStopTime", default=None)

    updateMethod: str = Field(alias="updateMethod")

    targets: List[Target] = Field(alias="targets")

    filterReference: Optional[FilterReference] = Field(alias="filterReference", default=None)

    catalogueReference: Optional[CatalogueReference] = Field(alias="catalogueReference", default=None)

    subscriptionExtension: Optional[_ExtensionType] = Field(alias="subscriptionExtension", default=None)
