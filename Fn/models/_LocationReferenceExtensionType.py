from typing import *

from pydantic import BaseModel, Field

from .Element import Element
from .FacilityLocation import FacilityLocation


class _LocationReferenceExtensionType(BaseModel):
    """
    None model

    """

    facilityLocation: Optional[FacilityLocation] = Field(alias="facilityLocation", default=None)

    anies: Optional[List[Optional[Element]]] = Field(alias="anies", default=None)
