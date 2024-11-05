from typing import *

from pydantic import BaseModel, Field

from .ForecastConditionReasonDtoV1 import ForecastConditionReasonDtoV1


class ForecastSectionWeatherForecastDtoV1(BaseModel):
    """
    None model
        Forecast section&#39;s weather forecast

    """

    time: Optional[str] = Field(alias="time", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    forecastName: Optional[str] = Field(alias="forecastName", default=None)

    daylight: Optional[bool] = Field(alias="daylight", default=None)

    roadTemperature: Optional[float] = Field(alias="roadTemperature", default=None)

    temperature: Optional[float] = Field(alias="temperature", default=None)

    windSpeed: Optional[float] = Field(alias="windSpeed", default=None)

    windDirection: Optional[int] = Field(alias="windDirection", default=None)

    overallRoadCondition: Optional[str] = Field(alias="overallRoadCondition", default=None)

    weatherSymbol: Optional[str] = Field(alias="weatherSymbol", default=None)

    reliability: Optional[str] = Field(alias="reliability", default=None)

    forecastConditionReason: Optional[ForecastConditionReasonDtoV1] = Field(
        alias="forecastConditionReason", default=None
    )

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
