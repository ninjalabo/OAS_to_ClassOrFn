from typing import *

from pydantic import BaseModel, Field


class GeometryObject(BaseModel):
    """
    None model
        GeoJson Geometry Object

    """

    type: str = Field(alias="type")

    coordinates: List[Dict[str, Any]] = Field(alias="coordinates")
