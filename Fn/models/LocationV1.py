from typing import *

from pydantic import BaseModel, Field


class LocationV1(BaseModel):
    """
    None model
        AlertC location of a traffic situation announcement

    """

    countryCode: int = Field(alias="countryCode")

    locationTableNumber: int = Field(alias="locationTableNumber")

    locationTableVersion: str = Field(alias="locationTableVersion")

    description: str = Field(alias="description")
