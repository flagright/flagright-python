# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .address import Address
from .amount import Amount
from .country_code import CountryCode
from .email_id import EmailId
from .tag import Tag

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class GenericBankAccountDetails(pydantic.BaseModel):
    """
    Model for any generic bank account
    """

    account_number: typing.Optional[str] = pydantic.Field(alias="accountNumber", description="Bank account number")
    account_type: typing.Optional[str] = pydantic.Field(
        alias="accountType", description="Bank account type. E.g. Checking, Savings etc."
    )
    account_balance: typing.Optional[Amount] = pydantic.Field(alias="accountBalance")
    bank_name: typing.Optional[str] = pydantic.Field(alias="bankName", description="Name of the bank")
    bank_code: typing.Optional[str] = pydantic.Field(
        alias="bankCode",
        description="Unique identifier of the bank. In some countries, this can be the same as the bank's SWIFT code",
    )
    country: typing.Optional[CountryCode]
    name: typing.Optional[str] = pydantic.Field(description="Name of the account holder")
    bank_address: typing.Optional[Address] = pydantic.Field(alias="bankAddress")
    email_id: typing.Optional[EmailId] = pydantic.Field(alias="emailId")
    special_instructions: typing.Optional[str] = pydantic.Field(
        alias="specialInstructions", description="Special instructions to be specified if any"
    )
    payment_channel: typing.Optional[str] = pydantic.Field(alias="paymentChannel")
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(
        description="Additional information that can be added via tags"
    )
    transit_number: typing.Optional[str] = pydantic.Field(
        alias="transitNumber", description="Transit number of the bank account"
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
