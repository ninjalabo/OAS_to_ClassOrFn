from typing import *

from pydantic import BaseModel, Field

from .AreaTypeV1 import AreaTypeV1


class AreaV1(BaseModel):
    """
    None model
        AlertC area

    """

    name: str = Field(alias="name")

    locationCode: int = Field(alias="locationCode")

    type: AreaTypeV1 = Field(alias="type")
