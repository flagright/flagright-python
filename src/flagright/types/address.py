# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .tag import Tag


class Address(pydantic.BaseModel):
    """
    Model for standardized address
    """

    address_lines: typing.List[typing.Any] = pydantic.Field(
        alias="addressLines", description=("Address lines of the user's residence address\n")
    )
    postcode: str = pydantic.Field(
        description=(
            'Post code of the user\'s residence address <span style="white-space: nowrap">`non-empty`</span> \n'
        )
    )
    city: str = pydantic.Field(
        description=('City of the user\'s residence address <span style="white-space: nowrap">`non-empty`</span> \n')
    )
    state: typing.Optional[str] = pydantic.Field(
        description=('State of the user\'s residence address <span style="white-space: nowrap">`non-empty`</span> \n')
    )
    country: str = pydantic.Field(
        description=('User\'s country of residence <span style="white-space: nowrap">`non-empty`</span> \n')
    )
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(
        description=("Additional information that can be added via tags\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
