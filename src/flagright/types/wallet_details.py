# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .amount import Amount
from .email_id import EmailId
from .tag import Tag
from .wallet_network import WalletNetwork

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class WalletDetails(pydantic.BaseModel):
    """
    Standardized model for a Generic wallet transaction
    """

    wallet_type: typing.Optional[str] = pydantic.Field(
        alias="walletType",
        description="Wallet type if there are various types of wallets belonging to the same user. E.g. Checking, savings, vault, different currency wallets etc.",
    )
    wallet_id: typing.Optional[str] = pydantic.Field(alias="walletId", description="Unique ID of the wallet")
    payment_channel: typing.Optional[str] = pydantic.Field(
        alias="paymentChannel", description="Payment Channel used through wallet"
    )
    name: typing.Optional[str] = pydantic.Field(description="Name of the account holder for a specific wallet")
    email_id: typing.Optional[EmailId] = pydantic.Field(alias="emailId")
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(
        description="Additional information that can be added via tags"
    )
    wallet_phone_number: typing.Optional[str] = pydantic.Field(
        alias="walletPhoneNumber", description="Phone number associated with the wallet, if any"
    )
    wallet_balance: typing.Optional[Amount] = pydantic.Field(alias="walletBalance")
    network: typing.Optional[WalletNetwork]

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
