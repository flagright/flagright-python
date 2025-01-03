# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .rule_action import RuleAction
from .rule_hit_meta import RuleHitMeta
from .rule_labels import RuleLabels
from .rule_nature import RuleNature

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class HitRulesDetails(pydantic.BaseModel):
    """
    Model for list of hit rules
    """

    rule_id: typing.Optional[str] = pydantic.Field(alias="ruleId", description="Unique rule identifier")
    rule_instance_id: str = pydantic.Field(alias="ruleInstanceId")
    rule_name: str = pydantic.Field(alias="ruleName", description="Name of the rule")
    rule_description: str = pydantic.Field(alias="ruleDescription", description="Description of the rule")
    executed_at: typing.Optional[float] = pydantic.Field(
        alias="executedAt", description="Timestamp when the rule was hit"
    )
    rule_action: RuleAction = pydantic.Field(alias="ruleAction")
    rule_hit_meta: typing.Optional[RuleHitMeta] = pydantic.Field(alias="ruleHitMeta")
    labels: typing.Optional[typing.List[RuleLabels]]
    nature: typing.Optional[RuleNature]
    is_shadow: typing.Optional[bool] = pydantic.Field(alias="isShadow")

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
