# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .list_metadata import ListMetadata
from .list_item import ListItem
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListData(UniversalBaseModel):
    """
    Payload of a list, new or existed
    """

    metadata: typing.Optional[ListMetadata] = None
    items: typing.Optional[typing.List[ListItem]] = pydantic.Field(default=None)
    """
    List items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
