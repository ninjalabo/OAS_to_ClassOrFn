from typing import *

from pydantic import BaseModel, Field

from .MeasurementSpecificCharacteristics import MeasurementSpecificCharacteristics


class _MeasurementSiteIndexMeasurementSpecificCharacteristics(BaseModel):
    """
    None model

    """

    measurementSpecificCharacteristics: MeasurementSpecificCharacteristics = Field(
        alias="measurementSpecificCharacteristics"
    )

    index: Optional[int] = Field(alias="index", default=None)
