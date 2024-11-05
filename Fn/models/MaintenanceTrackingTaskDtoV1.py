from typing import *

from pydantic import BaseModel, Field


class MaintenanceTrackingTaskDtoV1(BaseModel):
    """
    None model
        Maintenance tracking task

    """

    id: Optional[str] = Field(alias="id", default=None)

    nameFi: Optional[str] = Field(alias="nameFi", default=None)

    nameEn: Optional[str] = Field(alias="nameEn", default=None)

    nameSv: Optional[str] = Field(alias="nameSv", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
