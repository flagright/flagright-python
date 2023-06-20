# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .executed_rules_result import ExecutedRulesResult
from .hit_rules_details import HitRulesDetails
from .transaction import Transaction


class TransactionWithRulesResult(Transaction):
    """
    Model for transaction payload with rules result
    """

    executed_rules: typing.List[ExecutedRulesResult] = pydantic.Field(alias="executedRules")
    hit_rules: typing.List[HitRulesDetails] = pydantic.Field(alias="hitRules")

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
