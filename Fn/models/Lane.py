from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType
from ._LaneEnum import _LaneEnum


class Lane(BaseModel):
    """
    None model

    """

    laneNumber: Optional[int] = Field(alias="laneNumber", default=None)

    laneUsage: Optional[_LaneEnum] = Field(alias="laneUsage", default=None)

    get_LaneExtension: Optional[_ExtensionType] = Field(alias="get_LaneExtension", default=None)
