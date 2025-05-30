# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .legal_entity import LegalEntity
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class BusinessBase(UniversalBaseModel):
    """
    Model for a business user base fields
    """

    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId")] = pydantic.Field()
    """
    Unique user ID for the user
    """

    created_timestamp: typing_extensions.Annotated[float, FieldMetadata(alias="createdTimestamp")] = pydantic.Field()
    """
    Timestamp when the user was created
    """

    legal_entity: typing_extensions.Annotated[LegalEntity, FieldMetadata(alias="legalEntity")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
