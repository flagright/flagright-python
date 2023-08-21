# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .rule_failure_exception import RuleFailureException


class FailedRulesResult(pydantic.BaseModel):
    """
    Model for list of rules failed execution. It means rules could not be run
    """

    rule_id: str = pydantic.Field(
        alias="ruleId", description='Unique rule identifier <span style="white-space: nowrap">`non-empty`</span> '
    )
    rule_name: str = pydantic.Field(
        alias="ruleName", description='Name of the rule <span style="white-space: nowrap">`non-empty`</span> '
    )
    rule_description: str = pydantic.Field(
        alias="ruleDescription",
        description='Description of the rule <span style="white-space: nowrap">`non-empty`</span> ',
    )
    failure_exception: RuleFailureException = pydantic.Field(alias="failureException")

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
