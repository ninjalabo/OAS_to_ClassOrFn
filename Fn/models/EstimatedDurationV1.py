from typing import *

from pydantic import BaseModel, Field


class EstimatedDurationV1(BaseModel):
    """
    None model
        Announcement estimated duration

    """

    minimum: str = Field(alias="minimum")

    maximum: Optional[str] = Field(alias="maximum", default=None)

    informal: str = Field(alias="informal")
