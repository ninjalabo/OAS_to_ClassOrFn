from typing import *

from pydantic import BaseModel, Field


class ContactV1(BaseModel):
    """
    None model
        Sender&#39;s contact information

    """

    phone: Optional[str] = Field(alias="phone", default=None)

    email: Optional[str] = Field(alias="email", default=None)
