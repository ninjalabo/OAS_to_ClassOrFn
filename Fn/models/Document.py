from typing import *

from pydantic import BaseModel, Field

from .DocumentType import DocumentType
from .DOMConfiguration import DOMConfiguration
from .DOMImplementation import DOMImplementation
from .Element import Element
from .NamedNodeMap import NamedNodeMap
from .Node import Node
from .NodeList import NodeList


class Document(BaseModel):
    """
    None model

    """

    doctype: Optional[DocumentType] = Field(alias="doctype", default=None)

    documentElement: Optional[Element] = Field(alias="documentElement", default=None)

    inputEncoding: Optional[str] = Field(alias="inputEncoding", default=None)

    xmlEncoding: Optional[str] = Field(alias="xmlEncoding", default=None)

    xmlStandalone: Optional[bool] = Field(alias="xmlStandalone", default=None)

    xmlVersion: Optional[str] = Field(alias="xmlVersion", default=None)

    strictErrorChecking: Optional[bool] = Field(alias="strictErrorChecking", default=None)

    documentURI: Optional[str] = Field(alias="documentURI", default=None)

    domConfig: Optional[DOMConfiguration] = Field(alias="domConfig", default=None)

    implementation: Optional[DOMImplementation] = Field(alias="implementation", default=None)

    attributes: Optional[NamedNodeMap] = Field(alias="attributes", default=None)

    localName: Optional[str] = Field(alias="localName", default=None)

    nodeName: Optional[str] = Field(alias="nodeName", default=None)

    nodeValue: Optional[str] = Field(alias="nodeValue", default=None)

    parentNode: Optional[Node] = Field(alias="parentNode", default=None)

    childNodes: Optional[NodeList] = Field(alias="childNodes", default=None)

    firstChild: Optional[Node] = Field(alias="firstChild", default=None)

    lastChild: Optional[Node] = Field(alias="lastChild", default=None)

    previousSibling: Optional[Node] = Field(alias="previousSibling", default=None)

    nextSibling: Optional[Node] = Field(alias="nextSibling", default=None)

    ownerDocument: Optional["Document"] = Field(alias="ownerDocument", default=None)

    namespaceURI: Optional[str] = Field(alias="namespaceURI", default=None)

    baseURI: Optional[str] = Field(alias="baseURI", default=None)

    textContent: Optional[str] = Field(alias="textContent", default=None)

    prefix: Optional[str] = Field(alias="prefix", default=None)

    nodeType: Optional[int] = Field(alias="nodeType", default=None)
