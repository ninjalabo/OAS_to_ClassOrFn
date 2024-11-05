from typing import *

from pydantic import BaseModel, Field


class ForecastSectionPropertiesSimpleV1(BaseModel):
    """
    None model
        Simple forecast section properties

    """

    id: Optional[str] = Field(alias="id", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    roadSectionNumber: Optional[int] = Field(alias="roadSectionNumber", default=None)

    roadNumber: Optional[int] = Field(alias="roadNumber", default=None)

    roadSectionVersionNumber: Optional[int] = Field(alias="roadSectionVersionNumber", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
