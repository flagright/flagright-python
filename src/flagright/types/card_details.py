# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .card_brand import CardBrand
from .card_expiry import CardExpiry
from .card_funding import CardFunding
from .card_merchant_details import CardMerchantDetails
from .card_status import CardStatus
from .card_type import CardType
from .consumer_name import ConsumerName
from .country_code import CountryCode
from .email_id import EmailId
from .pos_details import PosDetails
from .tag import Tag

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CardDetails(pydantic.BaseModel):
    """
    Model for credit or debit card details
    """

    card_fingerprint: typing.Optional[str] = pydantic.Field(
        alias="cardFingerprint",
        description="Unique card fingerprint that helps identify a specific card without having to use explicit card number. This is likely available at your card payment scheme provider",
    )
    email_id: typing.Optional[EmailId] = pydantic.Field(alias="emailId")
    card_status: typing.Optional[CardStatus] = pydantic.Field(alias="cardStatus")
    card_issued_country: typing.Optional[CountryCode] = pydantic.Field(alias="cardIssuedCountry")
    transaction_reference_field: typing.Optional[str] = pydantic.Field(
        alias="transactionReferenceField", description="Reference for the transaction"
    )
    _3_ds_done: typing.Optional[bool] = pydantic.Field(
        alias="3dsDone", description="Whether 3ds was successfully enforced for the transaction"
    )
    name_on_card: typing.Optional[ConsumerName] = pydantic.Field(alias="nameOnCard")
    card_expiry: typing.Optional[CardExpiry] = pydantic.Field(alias="cardExpiry")
    pos_details: typing.Optional[PosDetails] = pydantic.Field(alias="posDetails")
    card_last_4_digits: typing.Optional[str] = pydantic.Field(
        alias="cardLast4Digits", description="Last 4 digits of Card"
    )
    card_brand: typing.Optional[CardBrand] = pydantic.Field(alias="cardBrand")
    card_funding: typing.Optional[CardFunding] = pydantic.Field(alias="cardFunding")
    card_authenticated: typing.Optional[bool] = pydantic.Field(
        alias="cardAuthenticated", description="Authentication of Card"
    )
    card_tokenized: typing.Optional[bool] = pydantic.Field(alias="cardTokenized", description="Was the card tokenized")
    card_present: typing.Optional[bool] = pydantic.Field(alias="cardPresent", description="Card Present")
    payment_channel: typing.Optional[str] = pydantic.Field(alias="paymentChannel")
    card_type: typing.Optional[CardType] = pydantic.Field(alias="cardType")
    merchant_details: typing.Optional[CardMerchantDetails] = pydantic.Field(alias="merchantDetails")
    network_provider_risk_score: typing.Optional[float] = pydantic.Field(
        alias="networkProviderRiskScore", description="Risk score of the card from your network provider"
    )
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
