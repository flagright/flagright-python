# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .transaction_type import TransactionType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TransactionBase(pydantic.BaseModel):
    """
    Model for transaction base Payload
    """

    type: TransactionType
    transaction_id: str = pydantic.Field(alias="transactionId", description="Unique transaction identifier")
    timestamp: float = pydantic.Field(description="Timestamp of when transaction took place")
    origin_user_id: typing.Optional[str] = pydantic.Field(
        alias="originUserId", description="UserId for where the transaction originates from"
    )
    destination_user_id: typing.Optional[str] = pydantic.Field(
        alias="destinationUserId",
        description="UserId for transaction's destination. In other words, where the value is being transferred to.",
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
