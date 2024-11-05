from typing import *

from pydantic import BaseModel, Field

from ._ExtensionType import _ExtensionType


class AxleCharacteristics(BaseModel):
    """
    None model

    """

    maximumWeight: Optional[float] = Field(alias="maximumWeight", default=None)

    minimumWeight: Optional[float] = Field(alias="minimumWeight", default=None)

    get_AxleCharacteristicsExtension: Optional[_ExtensionType] = Field(
        alias="get_AxleCharacteristicsExtension", default=None
    )
