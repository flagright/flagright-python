# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .address import Address
from .check_details_delivery_status import CheckDetailsDeliveryStatus
from .check_payment_method import CheckPaymentMethod


class CheckDetails(pydantic.BaseModel):
    method: CheckPaymentMethod
    check_number: typing.Optional[str] = pydantic.Field(alias="checkNumber")
    check_identifier: typing.Optional[str] = pydantic.Field(alias="checkIdentifier")
    name: typing.Optional[str]
    delivery_status: typing.Optional[CheckDetailsDeliveryStatus] = pydantic.Field(alias="deliveryStatus")
    eta_timestamp: typing.Optional[float] = pydantic.Field(alias="etaTimestamp")
    shipping_address: typing.Optional[Address] = pydantic.Field(alias="shippingAddress")

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
