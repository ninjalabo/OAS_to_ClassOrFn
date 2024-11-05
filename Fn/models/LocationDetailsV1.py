from typing import *

from pydantic import BaseModel, Field

from .AreaLocationV1 import AreaLocationV1
from .RoadAddressLocationV1 import RoadAddressLocationV1


class LocationDetailsV1(BaseModel):
    """
    None model
        LocationDetails

    """

    areaLocation: Optional[AreaLocationV1] = Field(alias="areaLocation", default=None)

    roadAddressLocation: Optional[RoadAddressLocationV1] = Field(alias="roadAddressLocation", default=None)
