from typing import *

from pydantic import BaseModel, Field


class MaintenanceTrackingDomainDtoV1(BaseModel):
    """
    None model
        Maintenance tracking domain

    """

    name: str = Field(alias="name")

    source: str = Field(alias="source")

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
