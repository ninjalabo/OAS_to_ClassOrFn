from typing import *

from pydantic import BaseModel, Field


class TypeInfo(BaseModel):
    """
    None model

    """

    typeName: Optional[str] = Field(alias="typeName", default=None)

    typeNamespace: Optional[str] = Field(alias="typeNamespace", default=None)
