# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .device_data import DeviceData
from .executed_rules_result import ExecutedRulesResult
from .hit_rules_details import HitRulesDetails
from .rule_action import RuleAction
from .transaction_risk_scoring_result import TransactionRiskScoringResult
from .transaction_state import TransactionState
from .transaction_updatable import TransactionUpdatable

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TransactionEventWithRulesResult(pydantic.BaseModel):
    transaction_state: TransactionState = pydantic.Field(alias="transactionState")
    timestamp: float = pydantic.Field(description="Timestamp of the event")
    transaction_id: str = pydantic.Field(alias="transactionId", description="Transaction ID the event pertains to")
    event_id: typing.Optional[str] = pydantic.Field(alias="eventId", description="Unique event ID")
    reason: typing.Optional[str] = pydantic.Field(description="Reason for the event or a state change")
    event_description: typing.Optional[str] = pydantic.Field(alias="eventDescription", description="Event description")
    updated_transaction_attributes: typing.Optional[TransactionUpdatable] = pydantic.Field(
        alias="updatedTransactionAttributes"
    )
    meta_data: typing.Optional[DeviceData] = pydantic.Field(alias="metaData")
    executed_rules: typing.Optional[typing.List[ExecutedRulesResult]] = pydantic.Field(alias="executedRules")
    hit_rules: typing.Optional[typing.List[HitRulesDetails]] = pydantic.Field(alias="hitRules")
    status: typing.Optional[RuleAction]
    risk_score_details: typing.Optional[TransactionRiskScoringResult] = pydantic.Field(alias="riskScoreDetails")

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
