# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .business_optional import BusinessOptional
from .executed_rules_result import ExecutedRulesResult
from .hit_rules_details import HitRulesDetails
from .user_risk_score_details import UserRiskScoreDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BusinessUserEventWithRulesResult(pydantic.BaseModel):
    timestamp: float = pydantic.Field(description="Timestamp of the event")
    user_id: str = pydantic.Field(alias="userId", description="Transaction ID the event pertains to")
    event_id: typing.Optional[str] = pydantic.Field(alias="eventId", description="Unique event ID")
    reason: typing.Optional[str] = pydantic.Field(description="Reason for the event or a state change")
    event_description: typing.Optional[str] = pydantic.Field(alias="eventDescription", description="Event description")
    updated_business_user_attributes: typing.Optional[BusinessOptional] = pydantic.Field(
        alias="updatedBusinessUserAttributes"
    )
    executed_rules: typing.Optional[typing.List[ExecutedRulesResult]] = pydantic.Field(alias="executedRules")
    hit_rules: typing.Optional[typing.List[HitRulesDetails]] = pydantic.Field(alias="hitRules")
    risk_score_details: typing.Optional[UserRiskScoreDetails] = pydantic.Field(alias="riskScoreDetails")

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
