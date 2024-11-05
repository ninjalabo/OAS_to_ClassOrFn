from typing import *

from pydantic import BaseModel, Field


class WeathercamPresetSimpleV1(BaseModel):
    """
    None model
        Weathercam preset object with basic information

    """

    id: Optional[str] = Field(alias="id", default=None)

    inCollection: Optional[bool] = Field(alias="inCollection", default=None)
