from typing import *

from pydantic import BaseModel, Field


class AlertCLocationV1(BaseModel):
    """
    None model
        AlertC location

    """

    locationCode: int = Field(alias="locationCode")

    name: str = Field(alias="name")

    distance: Optional[int] = Field(alias="distance", default=None)
