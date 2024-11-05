from typing import *

from pydantic import BaseModel, Field

from .DOMStringList import DOMStringList


class DOMConfiguration(BaseModel):
    """
    None model

    """

    parameterNames: Optional[DOMStringList] = Field(alias="parameterNames", default=None)
