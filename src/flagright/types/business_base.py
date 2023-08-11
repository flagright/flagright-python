# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .legal_entity import LegalEntity


class BusinessBase(pydantic.BaseModel):
    """
    Model for a business user base fields
    """

    user_id: str = pydantic.Field(
        alias="userId", description='Unique user ID for the user <span style="white-space: nowrap">`non-empty`</span> '
    )
    created_timestamp: float = pydantic.Field(
        alias="createdTimestamp", description="Timestamp when the user was created"
    )
    legal_entity: LegalEntity = pydantic.Field(alias="legalEntity")

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
