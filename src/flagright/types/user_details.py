# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .consumer_name import ConsumerName
from .country_code import CountryCode
from .gender import Gender

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UserDetails(pydantic.BaseModel):
    """
    Model for consumer user personal details
    """

    name: ConsumerName
    date_of_birth: typing.Optional[str] = pydantic.Field(
        alias="dateOfBirth", description="Date of birth of the user (YYYY-MM-DD)"
    )
    country_of_residence: typing.Optional[CountryCode] = pydantic.Field(alias="countryOfResidence")
    country_of_nationality: typing.Optional[CountryCode] = pydantic.Field(alias="countryOfNationality")
    gender: typing.Optional[Gender]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
