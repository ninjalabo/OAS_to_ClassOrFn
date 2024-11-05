from typing import *

from pydantic import BaseModel, Field

from .WeathercamPresetSimpleV1 import WeathercamPresetSimpleV1


class WeathercamStationPropertiesSimpleV1(BaseModel):
    """
    None model
        Weathercam station properties object with basic information

    """

    id: str = Field(alias="id")

    name: Optional[str] = Field(alias="name", default=None)

    collectionStatus: Optional[str] = Field(alias="collectionStatus", default=None)

    state: Optional[str] = Field(alias="state", default=None)

    dataUpdatedTime: Optional[str] = Field(alias="dataUpdatedTime", default=None)

    presets: Optional[List[Optional[WeathercamPresetSimpleV1]]] = Field(alias="presets", default=None)
