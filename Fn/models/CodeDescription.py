from typing import *

from pydantic import BaseModel, Field


class CodeDescription(BaseModel):
    """
    None model
        Description of code

    """

    description: str = Field(alias="description")

    descriptionEn: str = Field(alias="descriptionEn")

    code: str = Field(alias="code")
