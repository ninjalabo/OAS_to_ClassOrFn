from typing import *

from pydantic import BaseModel, Field


class DomainsResponseModel(BaseModel):
    """
    None model
        Counting Site Domain

    """

    addedTimestamp: Optional[str] = Field(alias="addedTimestamp", default=None)

    name: Optional[str] = Field(alias="name", default=None)

    description: Optional[str] = Field(alias="description", default=None)

    removedTimestamp: Optional[str] = Field(alias="removedTimestamp", default=None)
