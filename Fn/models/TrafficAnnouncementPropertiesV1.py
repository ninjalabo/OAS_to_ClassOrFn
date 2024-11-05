from typing import *

from pydantic import BaseModel, Field

from .ContactV1 import ContactV1
from .SituationTypeV1 import SituationTypeV1
from .TrafficAnnouncementV1 import TrafficAnnouncementV1


class TrafficAnnouncementPropertiesV1(BaseModel):
    """
    None model
        Traffic Announcement properties

    """

    situationId: str = Field(alias="situationId")

    situationType: SituationTypeV1 = Field(alias="situationType")

    trafficAnnouncementType: Optional[str] = Field(alias="trafficAnnouncementType", default=None)

    version: int = Field(alias="version")

    releaseTime: str = Field(alias="releaseTime")

    versionTime: str = Field(alias="versionTime")

    announcements: List[TrafficAnnouncementV1] = Field(alias="announcements")

    contact: Optional[ContactV1] = Field(alias="contact", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
