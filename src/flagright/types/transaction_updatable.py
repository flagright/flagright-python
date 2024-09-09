# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .device_data import DeviceData
from .origin_funds_info import OriginFundsInfo
from .tag import Tag
from .transaction_amount_details import TransactionAmountDetails
from .transaction_state import TransactionState
from .transaction_updatable_destination_payment_details import TransactionUpdatableDestinationPaymentDetails
from .transaction_updatable_origin_payment_details import TransactionUpdatableOriginPaymentDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TransactionUpdatable(pydantic.BaseModel):
    """
    Model for transaction additional payload
    """

    transaction_state: typing.Optional[TransactionState] = pydantic.Field(alias="transactionState")
    origin_amount_details: typing.Optional[TransactionAmountDetails] = pydantic.Field(alias="originAmountDetails")
    destination_amount_details: typing.Optional[TransactionAmountDetails] = pydantic.Field(
        alias="destinationAmountDetails"
    )
    origin_payment_details: typing.Optional[TransactionUpdatableOriginPaymentDetails] = pydantic.Field(
        alias="originPaymentDetails",
        description="Payment details of the origin. It can be a bank account number, wallet ID, card fingerprint etc.",
    )
    destination_payment_details: typing.Optional[TransactionUpdatableDestinationPaymentDetails] = pydantic.Field(
        alias="destinationPaymentDetails"
    )
    origin_funds_info: typing.Optional[OriginFundsInfo] = pydantic.Field(alias="originFundsInfo")
    related_transaction_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="relatedTransactionIds",
        description="IDs of transactions related to this transaction. Ex: refund, split bills",
    )
    product_type: typing.Optional[str] = pydantic.Field(
        alias="productType", description="Type of produce being used by the consumer (ex wallets, payments etc)"
    )
    promotion_code_used: typing.Optional[bool] = pydantic.Field(
        alias="promotionCodeUsed", description="Whether a promotion code was used or not the transaction"
    )
    reference: typing.Optional[str] = pydantic.Field(
        description="Reference field for the transaction indicating the purpose of the transaction etc."
    )
    origin_device_data: typing.Optional[DeviceData] = pydantic.Field(alias="originDeviceData")
    destination_device_data: typing.Optional[DeviceData] = pydantic.Field(alias="destinationDeviceData")
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
