from typing import *

from pydantic import BaseModel, Field


class WorkTypeV1(BaseModel):
    """
    None model
        Work type

    """

    type: str = Field(alias="type")

    description: str = Field(alias="description")
