from typing import *

from pydantic import BaseModel, Field


class LocationPropertiesV1(BaseModel):
    """
    None model
        Location GeoJSON properties object

    """

    locationCode: int = Field(alias="locationCode")

    subtypeCode: str = Field(alias="subtypeCode")

    roadJunction: Optional[str] = Field(alias="roadJunction", default=None)

    roadName: Optional[str] = Field(alias="roadName", default=None)

    firstName: str = Field(alias="firstName")

    secondName: Optional[str] = Field(alias="secondName", default=None)

    areaRef: Optional[int] = Field(alias="areaRef", default=None)

    linearRef: Optional[int] = Field(alias="linearRef", default=None)

    negOffset: Optional[int] = Field(alias="negOffset", default=None)

    posOffset: Optional[int] = Field(alias="posOffset", default=None)

    urban: Optional[bool] = Field(alias="urban", default=None)

    coordinatesETRS89: Optional[List[float]] = Field(alias="coordinatesETRS89", default=None)

    negDirection: Optional[str] = Field(alias="negDirection", default=None)

    posDirection: Optional[str] = Field(alias="posDirection", default=None)

    geocode: Optional[str] = Field(alias="geocode", default=None)

    orderOfPoint: Optional[str] = Field(alias="orderOfPoint", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    locationVersion: Optional[str] = Field(alias="locationVersion", default=None)
