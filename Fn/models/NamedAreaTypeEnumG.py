from typing import *

from pydantic import BaseModel, Field


class NamedAreaTypeEnumG(BaseModel):
    """
    None model

    """

    value: str = Field(alias="value")

    extendedValueG: Optional[str] = Field(alias="extendedValueG", default=None)
