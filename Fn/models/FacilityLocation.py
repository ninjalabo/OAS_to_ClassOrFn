from typing import *

from pydantic import BaseModel, Field

from .Address import Address


class FacilityLocation(BaseModel):
    """
    None model

    """

    timeZone: Optional[str] = Field(alias="timeZone", default=None)

    address: Optional[Address] = Field(alias="address", default=None)
