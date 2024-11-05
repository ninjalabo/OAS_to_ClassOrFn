from typing import *

from pydantic import BaseModel, Field


class WeathercamPresetHistoryItemDtoV1(BaseModel):
    """
    None model
        Weather camera preset&#39;s image history details.

    """

    lastModified: Optional[str] = Field(alias="lastModified", default=None)

    imageUrl: Optional[str] = Field(alias="imageUrl", default=None)

    sizeBytes: Optional[int] = Field(alias="sizeBytes", default=None)
