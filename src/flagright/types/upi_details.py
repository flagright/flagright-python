# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .tag import Tag
from .upi_payment_method import UpiPaymentMethod


class UpiDetails(pydantic.BaseModel):
    """
    Model for UPI payment method
    """

    method: UpiPaymentMethod
    upi_id: str = pydantic.Field(
        alias="upiID", description='UPI Id number <span style="white-space: nowrap">`non-empty`</span> '
    )
    bank_provider: typing.Optional[str] = pydantic.Field(
        alias="bankProvider", description='Bank provider name <span style="white-space: nowrap">`non-empty`</span> '
    )
    interface_provider: typing.Optional[str] = pydantic.Field(
        alias="interfaceProvider",
        description='Interface provider name <span style="white-space: nowrap">`non-empty`</span> ',
    )
    name: typing.Optional[str] = pydantic.Field(description="Name of the account holder")
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(
        description="Additional information that can be added via tags"
    )

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
