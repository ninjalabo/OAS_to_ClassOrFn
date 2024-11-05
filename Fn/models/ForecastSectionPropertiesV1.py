from typing import *

from pydantic import BaseModel, Field

from .RoadSegmentDtoV1 import RoadSegmentDtoV1


class ForecastSectionPropertiesV1(BaseModel):
    """
    None model
        Forecast Section Properties

    """

    id: Optional[str] = Field(alias="id", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    roadSectionNumber: Optional[int] = Field(alias="roadSectionNumber", default=None)

    roadNumber: Optional[int] = Field(alias="roadNumber", default=None)

    length: Optional[int] = Field(alias="length", default=None)

    roadSegments: Optional[List[Optional[RoadSegmentDtoV1]]] = Field(alias="roadSegments", default=None)

    linkIds: Optional[List[int]] = Field(alias="linkIds", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
