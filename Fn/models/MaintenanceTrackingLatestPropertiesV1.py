from typing import *

from pydantic import BaseModel, Field


class MaintenanceTrackingLatestPropertiesV1(BaseModel):
    """
    None model
        Maintenance tracking properties

    """

    id: int = Field(alias="id")

    time: str = Field(alias="time")

    created: str = Field(alias="created")

    tasks: List[str] = Field(alias="tasks")

    direction: Optional[float] = Field(alias="direction", default=None)

    domain: Optional[str] = Field(alias="domain", default=None)

    source: Optional[str] = Field(alias="source", default=None)
