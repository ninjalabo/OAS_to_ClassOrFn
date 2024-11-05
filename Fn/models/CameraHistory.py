from typing import *

from pydantic import BaseModel, Field

from .PresetHistory import PresetHistory


class CameraHistory(BaseModel):
    """
    None model
        Weather camera&#39;s image history details.

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    stations: Optional[List[Optional[PresetHistory]]] = Field(alias="stations", default=None)
