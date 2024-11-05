from typing import *

from pydantic import BaseModel, Field

from .AlertCLocationV1 import AlertCLocationV1
from .TrafficMessageRoadAddressV1 import TrafficMessageRoadAddressV1


class RoadPointV1(BaseModel):
    """
    None model
        A single road point

    """

    municipality: Optional[str] = Field(alias="municipality", default=None)

    province: Optional[str] = Field(alias="province", default=None)

    country: Optional[str] = Field(alias="country", default=None)

    roadAddress: TrafficMessageRoadAddressV1 = Field(alias="roadAddress")

    roadName: Optional[str] = Field(alias="roadName", default=None)

    alertCLocation: AlertCLocationV1 = Field(alias="alertCLocation")
