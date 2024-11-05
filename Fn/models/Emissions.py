from typing import *

from pydantic import BaseModel, Field

from ._EmissionClassificationEuroEnum import _EmissionClassificationEuroEnum
from ._EmissionsExtensionType import _EmissionsExtensionType
from ._LowEmissionLevelEnum import _LowEmissionLevelEnum


class Emissions(BaseModel):
    """
    None model

    """

    emissionClassificationEuro: Optional[_EmissionClassificationEuroEnum] = Field(
        alias="emissionClassificationEuro", default=None
    )

    emissionClassificationOthers: Optional[List[str]] = Field(alias="emissionClassificationOthers", default=None)

    emissionLevel: Optional[_LowEmissionLevelEnum] = Field(alias="emissionLevel", default=None)

    get_EmissionsExtension: Optional[_EmissionsExtensionType] = Field(alias="get_EmissionsExtension", default=None)
