# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .consumer_name import ConsumerName
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .country_code import CountryCode
from .gender import Gender
from .marital_status import MaritalStatus
from .place_of_birth import PlaceOfBirth
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UserDetails(UniversalBaseModel):
    """
    Model for consumer user personal details
    """

    name: typing.Optional[ConsumerName] = None
    date_of_birth: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dateOfBirth")] = (
        pydantic.Field(default=None)
    )
    """
    Date of birth of the user (YYYY-MM-DD)
    """

    user_category: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="userCategory")] = (
        pydantic.Field(default=None)
    )
    """
    Internal category of the user
    """

    country_of_residence: typing_extensions.Annotated[
        typing.Optional[CountryCode], FieldMetadata(alias="countryOfResidence")
    ] = None
    country_of_tax_residence: typing_extensions.Annotated[
        typing.Optional[CountryCode], FieldMetadata(alias="countryOfTaxResidence")
    ] = None
    country_of_nationality: typing_extensions.Annotated[
        typing.Optional[CountryCode], FieldMetadata(alias="countryOfNationality")
    ] = None
    gender: typing.Optional[Gender] = None
    marital_status: typing_extensions.Annotated[
        typing.Optional[MaritalStatus], FieldMetadata(alias="maritalStatus")
    ] = None
    place_of_birth: typing_extensions.Annotated[typing.Optional[PlaceOfBirth], FieldMetadata(alias="placeOfBirth")] = (
        None
    )
    alias: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Alias names of the user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
