from typing import *

from pydantic import BaseModel, Field

from .AreaV1 import AreaV1


class AreaLocationV1(BaseModel):
    """
    None model
        Location consisting of one or more areas

    """

    areas: List[AreaV1] = Field(alias="areas")
