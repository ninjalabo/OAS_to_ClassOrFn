from typing import *

from pydantic import BaseModel, Field

from .RoadPointV1 import RoadPointV1


class RoadAddressLocationV1(BaseModel):
    """
    None model
        Location consisting of a single road point or a road segment between two road points

    """

    primaryPoint: RoadPointV1 = Field(alias="primaryPoint")

    secondaryPoint: Optional[RoadPointV1] = Field(alias="secondaryPoint", default=None)

    direction: str = Field(alias="direction")

    directionDescription: Optional[str] = Field(alias="directionDescription", default=None)
