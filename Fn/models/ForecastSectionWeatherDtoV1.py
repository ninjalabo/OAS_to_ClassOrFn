from typing import *

from pydantic import BaseModel, Field

from .ForecastSectionWeatherForecastDtoV1 import ForecastSectionWeatherForecastDtoV1


class ForecastSectionWeatherDtoV1(BaseModel):
    """
    None model
        Forecast section weather forecasts

    """

    id: Optional[str] = Field(alias="id", default=None)

    forecasts: Optional[List[Optional[ForecastSectionWeatherForecastDtoV1]]] = Field(alias="forecasts", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
