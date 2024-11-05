from typing import *

from pydantic import BaseModel, Field


class TmsSensorConstantValueDtoV1(BaseModel):
    """
    None model
        Sensor constant value

    """

    name: str = Field(alias="name")

    value: int = Field(alias="value")

    validFrom: str = Field(alias="validFrom")

    validTo: str = Field(alias="validTo")
