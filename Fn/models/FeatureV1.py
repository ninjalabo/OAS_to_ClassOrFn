from typing import *

from pydantic import BaseModel, Field

from .TimeAndDurationV1 import TimeAndDurationV1


class FeatureV1(BaseModel):
    """
    None model
        Characteristics and qualities of the situation

    """

    name: str = Field(alias="name")

    quantity: Optional[float] = Field(alias="quantity", default=None)

    unit: Optional[str] = Field(alias="unit", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    timeAndDuration: Optional[TimeAndDurationV1] = Field(alias="timeAndDuration", default=None)
