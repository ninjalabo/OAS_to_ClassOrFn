from typing import *

from pydantic import BaseModel, Field

from .AreaTypeV1 import AreaTypeV1


class RegionGeometryPropertiesV1(BaseModel):
    """
    None model
        Region geometry properties

    """

    locationCode: int = Field(alias="locationCode")

    name: str = Field(alias="name")

    type: AreaTypeV1 = Field(alias="type")

    effectiveDate: str = Field(alias="effectiveDate")
