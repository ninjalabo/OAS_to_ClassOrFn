from typing import *

from pydantic import BaseModel, Field

from .FeatureV1 import FeatureV1


class RestrictionV1(BaseModel):
    """
    None model
        A single phase in a larger road work

    """

    type: Optional[str] = Field(alias="type", default=None)

    restriction: Optional[FeatureV1] = Field(alias="restriction", default=None)
