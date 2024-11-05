from typing import *

from pydantic import BaseModel, Field

from .CodeDescription import CodeDescription


class VariableSignDescriptions(BaseModel):
    """
    None model

    """

    signTypes: Optional[List[Optional[CodeDescription]]] = Field(alias="signTypes", default=None)

    dataUpdatedTime: str = Field(alias="dataUpdatedTime")
