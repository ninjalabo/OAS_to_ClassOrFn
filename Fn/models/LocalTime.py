from typing import *

from pydantic import BaseModel, Field


class LocalTime(BaseModel):
    """
    None model
        End time of the time period in ISO 8601 local time in Europe/Helsinki

    """

    hour: Optional[int] = Field(alias="hour", default=None)

    minute: Optional[int] = Field(alias="minute", default=None)

    second: Optional[int] = Field(alias="second", default=None)

    nano: Optional[int] = Field(alias="nano", default=None)
