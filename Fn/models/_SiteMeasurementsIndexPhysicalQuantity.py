from typing import *

from pydantic import BaseModel, Field

from .PhysicalQuantity import PhysicalQuantity


class _SiteMeasurementsIndexPhysicalQuantity(BaseModel):
    """
    None model

    """

    physicalQuantity: PhysicalQuantity = Field(alias="physicalQuantity")

    index: Optional[int] = Field(alias="index", default=None)
