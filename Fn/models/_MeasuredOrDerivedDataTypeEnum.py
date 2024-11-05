from typing import *

from pydantic import BaseModel, Field


class _MeasuredOrDerivedDataTypeEnum(BaseModel):
    """
    None model

    """

    value: Optional[str] = Field(alias="value", default=None)

    get_ExtendedValue: Optional[str] = Field(alias="get_ExtendedValue", default=None)
