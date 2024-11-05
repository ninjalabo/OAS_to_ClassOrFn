from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetDirectionV1 import WeathercamPresetDirectionV1


class WeathercamPresetDetailedV1(BaseModel):
    """
    None model
        Weathercam preset object with detailed information

    """

    id: Optional[str] = Field(alias="id", default=None)

    presentationName: Optional[str] = Field(alias="presentationName", default=None)

    inCollection: Optional[bool] = Field(alias="inCollection", default=None)

    resolution: Optional[str] = Field(alias="resolution", default=None)

    directionCode: str = Field(alias="directionCode")

    imageUrl: Optional[str] = Field(alias="imageUrl", default=None)

    direction: WeathercamPresetDirectionV1 = Field(alias="direction")
