from typing import *

from pydantic import BaseModel, Field

from .RoadStationSensorDirection import RoadStationSensorDirection
from .SensorValueDescription import SensorValueDescription


class WeatherStationSensorDtoV1(BaseModel):
    """
    None model
        Weather road station sensor

    """

    id: int = Field(alias="id")

    name: Optional[str] = Field(alias="name", default=None)

    shortName: Optional[str] = Field(alias="shortName", default=None)

    unit: Optional[str] = Field(alias="unit", default=None)

    accuracy: Optional[int] = Field(alias="accuracy", default=None)

    sensorValueDescriptions: Optional[List[Optional[SensorValueDescription]]] = Field(
        alias="sensorValueDescriptions", default=None
    )

    presentationNames: Optional[Dict[str, Any]] = Field(alias="presentationNames", default=None)

    descriptions: Optional[Dict[str, Any]] = Field(alias="descriptions", default=None)

    direction: Optional[RoadStationSensorDirection] = Field(alias="direction", default=None)

    description: Optional[str] = Field(alias="description", default=None)
