from typing import *

from pydantic import BaseModel, Field


class WeathercamPresetPublicityHistoryV1(BaseModel):
    """
    None model
        Weathercam station preset&#39;s publicity changes

    """

    id: str = Field(alias="id")

    measuredTime: Optional[str] = Field(alias="measuredTime", default=None)

    publishableTo: Optional[bool] = Field(alias="publishableTo", default=None)

    modifiedTime: Optional[str] = Field(alias="modifiedTime", default=None)
