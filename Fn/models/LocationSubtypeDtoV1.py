from typing import *

from pydantic import BaseModel, Field


class LocationSubtypeDtoV1(BaseModel):
    """
    None model
        Location subtype

    """

    subtypeCode: str = Field(alias="subtypeCode")

    descriptionFi: str = Field(alias="descriptionFi")

    descriptionEn: str = Field(alias="descriptionEn")
