from typing import *

from pydantic import BaseModel, Field


class _MeasurementSiteVersionedReference(BaseModel):
    """
    None model

    """

    id: Optional[str] = Field(alias="id", default=None)

    version: Optional[str] = Field(alias="version", default=None)
