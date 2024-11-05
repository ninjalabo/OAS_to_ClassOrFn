# coding: utf-8

"""
    Digitraffic Road API

    [OpenAPI document](/swagger/openapi.json)   Digitraffic is a service operated by the [Fintraffic](https://www.fintraffic.fi) offering real time traffic information. Currently the service covers *road, marine and rail* traffic. More information can be found at the [Digitraffic website](https://www.digitraffic.fi/)   The service has a public Google-group [road.digitraffic.fi](https://groups.google.com/forum/#!forum/roaddigitrafficfi) for communication between developers, service administrators and Fintraffic. The discussion in the forum is mostly in Finnish, but you're welcome to communicate in English too.   ### General notes of the API * Many Digitraffic APIs use GeoJSON as data format. Definition of the GeoJSON format can be found at https://tools.ietf.org/html/rfc7946. * For dates and times [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format is used with \"Zulu\" zero offset from UTC unless otherwise specified (i.e., \"yyyy-mm-ddThh:mm:ss[.mmm]Z\"). E.g. 2019-11-01T06:30:00Z.

    The version of the OpenAPI document: Branch: master, tag: 2024.10.28-1 #ef5bdf3 @ 2024-10-29T08:05:03+0000
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.extension_type import ExtensionType
from openapi_client.models.international_identifier import InternationalIdentifier
from openapi_client.models.location_reference import LocationReference
from openapi_client.models.multilingual_string import MultilingualString
from openapi_client.models.physical_quantity_fault import PhysicalQuantityFault
from openapi_client.models.source import Source
from typing import Optional, Set
from typing_extensions import Self

class PhysicalQuantity(BaseModel):
    """
    PhysicalQuantity
    """ # noqa: E501
    forecast: Optional[StrictBool] = None
    measurement_equipment_type_used: Optional[MultilingualString] = Field(default=None, alias="measurementEquipmentTypeUsed")
    pertinent_location: Optional[LocationReference] = Field(default=None, alias="pertinentLocation")
    physical_quantity_faults: Optional[List[PhysicalQuantityFault]] = Field(default=None, alias="physicalQuantityFaults")
    source: Optional[Source] = None
    information_manager_override: Optional[InternationalIdentifier] = Field(default=None, alias="informationManagerOverride")
    get_physical_quantity_extension: Optional[ExtensionType] = Field(default=None, alias="get_PhysicalQuantityExtension")
    __properties: ClassVar[List[str]] = ["forecast", "measurementEquipmentTypeUsed", "pertinentLocation", "physicalQuantityFaults", "source", "informationManagerOverride", "get_PhysicalQuantityExtension"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PhysicalQuantity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of measurement_equipment_type_used
        if self.measurement_equipment_type_used:
            _dict['measurementEquipmentTypeUsed'] = self.measurement_equipment_type_used.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pertinent_location
        if self.pertinent_location:
            _dict['pertinentLocation'] = self.pertinent_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in physical_quantity_faults (list)
        _items = []
        if self.physical_quantity_faults:
            for _item in self.physical_quantity_faults:
                if _item:
                    _items.append(_item.to_dict())
            _dict['physicalQuantityFaults'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of information_manager_override
        if self.information_manager_override:
            _dict['informationManagerOverride'] = self.information_manager_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of get_physical_quantity_extension
        if self.get_physical_quantity_extension:
            _dict['get_PhysicalQuantityExtension'] = self.get_physical_quantity_extension.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalQuantity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forecast": obj.get("forecast"),
            "measurementEquipmentTypeUsed": MultilingualString.from_dict(obj["measurementEquipmentTypeUsed"]) if obj.get("measurementEquipmentTypeUsed") is not None else None,
            "pertinentLocation": LocationReference.from_dict(obj["pertinentLocation"]) if obj.get("pertinentLocation") is not None else None,
            "physicalQuantityFaults": [PhysicalQuantityFault.from_dict(_item) for _item in obj["physicalQuantityFaults"]] if obj.get("physicalQuantityFaults") is not None else None,
            "source": Source.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "informationManagerOverride": InternationalIdentifier.from_dict(obj["informationManagerOverride"]) if obj.get("informationManagerOverride") is not None else None,
            "get_PhysicalQuantityExtension": ExtensionType.from_dict(obj["get_PhysicalQuantityExtension"]) if obj.get("get_PhysicalQuantityExtension") is not None else None
        })
        return _obj

