# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .executed_rules_result import ExecutedRulesResult
from .hit_rules_details import HitRulesDetails
from .user_risk_score_details import UserRiskScoreDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BusinessUserMonitoringResult(pydantic.BaseModel):
    """
    Model for business user risk score response
    """

    user_id: str = pydantic.Field(alias="userId", description="user ID the risk score pertains to")
    risk_score_details: typing.Optional[UserRiskScoreDetails] = pydantic.Field(alias="riskScoreDetails")
    hit_rules: typing.Optional[typing.List[HitRulesDetails]] = pydantic.Field(alias="hitRules")
    executed_rules: typing.Optional[typing.List[ExecutedRulesResult]] = pydantic.Field(alias="executedRules")

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