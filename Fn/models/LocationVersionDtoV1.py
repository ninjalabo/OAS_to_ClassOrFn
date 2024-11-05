from typing import *

from pydantic import BaseModel, Field


class LocationVersionDtoV1(BaseModel):
    """
    None model
        Location Version Object

    """

    version: str = Field(alias="version")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
