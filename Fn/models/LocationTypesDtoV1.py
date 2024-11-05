from typing import *

from pydantic import BaseModel, Field

from .LocationSubtypeDtoV1 import LocationSubtypeDtoV1
from .LocationTypeDtoV1 import LocationTypeDtoV1


class LocationTypesDtoV1(BaseModel):
    """
    None model
        TMS/Alert-C Location types and location subtypes

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    version: str = Field(alias="version")

    locationTypes: List[LocationTypeDtoV1] = Field(alias="locationTypes")

    locationSubtypes: List[LocationSubtypeDtoV1] = Field(alias="locationSubtypes")
