from typing import *

from pydantic import BaseModel, Field


class ForecastConditionReasonDtoV1(BaseModel):
    """
    None model
        Forecast that is used is Vaisala’s weather forecast which is initialised from the weather model that performs best for Finland for a period under study. Majority of the times the initialisation is done from ECMWF model data. Then Vaisala meteorologists also manually edit the data to fix certain known errors in the model.

    """

    precipitationCondition: Optional[str] = Field(alias="precipitationCondition", default=None)

    roadCondition: Optional[str] = Field(alias="roadCondition", default=None)

    windCondition: Optional[str] = Field(alias="windCondition", default=None)

    freezingRainCondition: Optional[bool] = Field(alias="freezingRainCondition", default=None)

    winterSlipperiness: Optional[bool] = Field(alias="winterSlipperiness", default=None)

    visibilityCondition: Optional[str] = Field(alias="visibilityCondition", default=None)

    frictionCondition: Optional[str] = Field(alias="frictionCondition", default=None)
