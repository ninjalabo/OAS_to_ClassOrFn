from typing import *

from pydantic import BaseModel, Field


class LocationTypeDtoV1(BaseModel):
    """
    None model
        Location type

    """

    typeCode: str = Field(alias="typeCode")

    descriptionFi: str = Field(alias="descriptionFi")

    descriptionEn: str = Field(alias="descriptionEn")
