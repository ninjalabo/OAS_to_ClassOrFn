from typing import *

from pydantic import BaseModel, Field


class WeathercamPresetDataV1(BaseModel):
    """
    None model
        Weathercam preset&#39;s latest image capture data

    """

    id: str = Field(alias="id")

    measuredTime: str = Field(alias="measuredTime")
