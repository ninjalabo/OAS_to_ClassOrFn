from typing import *

from pydantic import BaseModel, Field

from .SignTextRowV1 import SignTextRowV1


class VariableSignPropertiesV1(BaseModel):
    """
    None model
        Variable Sign properties

    """

    id: Optional[str] = Field(alias="id", default=None)

    type: Optional[str] = Field(alias="type", default=None)

    roadAddress: Optional[str] = Field(alias="roadAddress", default=None)

    direction: Optional[str] = Field(alias="direction", default=None)

    carriageway: Optional[str] = Field(alias="carriageway", default=None)

    displayValue: Optional[str] = Field(alias="displayValue", default=None)

    additionalInformation: Optional[str] = Field(alias="additionalInformation", default=None)

    effectDate: Optional[str] = Field(alias="effectDate", default=None)

    cause: Optional[str] = Field(alias="cause", default=None)

    reliability: Optional[str] = Field(alias="reliability", default=None)

    textRows: Optional[List[Optional[SignTextRowV1]]] = Field(alias="textRows", default=None)
