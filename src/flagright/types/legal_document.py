# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .country_code import CountryCode
from .tag import Tag
from .consumer_name import ConsumerName
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LegalDocument(UniversalBaseModel):
    """
    LegalDocument model generalizes User's identity document type (ex: Passport)
    """

    document_type: typing_extensions.Annotated[str, FieldMetadata(alias="documentType")] = pydantic.Field()
    """
    User's identity document type such as passport, national ID etc.
    """

    document_number: typing_extensions.Annotated[str, FieldMetadata(alias="documentNumber")] = pydantic.Field()
    """
    User's unique identity document number such as passport number
    """

    document_issued_date: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="documentIssuedDate")
    ] = pydantic.Field(default=None)
    """
    User's identity document issuance date (UNIX timestamp in milliseconds)
    """

    document_expiration_date: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="documentExpirationDate")
    ] = pydantic.Field(default=None)
    """
    User's identity document expiration date (UNIX timestamp in milliseconds)
    """

    document_issued_country: typing_extensions.Annotated[CountryCode, FieldMetadata(alias="documentIssuedCountry")]
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(default=None)
    """
    Additional information that can be added via tags
    """

    name_on_document: typing_extensions.Annotated[
        typing.Optional[ConsumerName], FieldMetadata(alias="nameOnDocument")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
