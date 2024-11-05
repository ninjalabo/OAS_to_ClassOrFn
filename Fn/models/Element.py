from typing import *

from pydantic import BaseModel, Field

from .Attr import Attr
from .Document import Document
from .NamedNodeMap import NamedNodeMap
from .Node import Node
from .NodeList import NodeList
from .TypeInfo import TypeInfo


class Element(BaseModel):
    """
    None model

    """

    schemaTypeInfo: Optional[TypeInfo] = Field(alias="schemaTypeInfo", default=None)

    attributeNodeNS: Optional[Attr] = Field(alias="attributeNodeNS", default=None)

    attributeNode: Optional[Attr] = Field(alias="attributeNode", default=None)

    tagName: Optional[str] = Field(alias="tagName", default=None)

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

    ownerDocument: Optional[Document] = Field(alias="ownerDocument", default=None)

    namespaceURI: Optional[str] = Field(alias="namespaceURI", default=None)

    baseURI: Optional[str] = Field(alias="baseURI", default=None)

    textContent: Optional[str] = Field(alias="textContent", default=None)

    prefix: Optional[str] = Field(alias="prefix", default=None)

    nodeType: Optional[int] = Field(alias="nodeType", default=None)