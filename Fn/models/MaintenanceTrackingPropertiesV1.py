from typing import *

from pydantic import BaseModel, Field


class MaintenanceTrackingPropertiesV1(BaseModel):
    """
    None model
        Maintenance tracking properties

    """

    id: int = Field(alias="id")

    previousId: Optional[int] = Field(alias="previousId", default=None)

    sendingTime: str = Field(alias="sendingTime")

    created: str = Field(alias="created")

    tasks: List[str] = Field(alias="tasks")

    startTime: str = Field(alias="startTime")

    endTime: str = Field(alias="endTime")

    direction: Optional[float] = Field(alias="direction", default=None)

    domain: Optional[str] = Field(alias="domain", default=None)

    source: Optional[str] = Field(alias="source", default=None)
