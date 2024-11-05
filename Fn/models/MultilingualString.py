from typing import *

from pydantic import BaseModel, Field

from .Values import Values


class MultilingualString(BaseModel):
    """
    None model

    """

    values: Values = Field(alias="values")
