from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionWeatherDtoV1 import ForecastSectionWeatherDtoV1


class ForecastSectionsWeatherDtoV1(BaseModel):
    """
    None model

    """

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")

    forecastSections: Optional[List[Optional[ForecastSectionWeatherDtoV1]]] = Field(
        alias="forecastSections", default=None
    )
