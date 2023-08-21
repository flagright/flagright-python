# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .false_positive_details import FalsePositiveDetails
from .rule_hit_direction import RuleHitDirection
from .sanctions_details import SanctionsDetails


class RuleHitMeta(pydantic.BaseModel):
    """
    Details of rule execution, for internal purposes only
    """

    hit_directions: typing.Optional[typing.List[RuleHitDirection]] = pydantic.Field(alias="hitDirections")
    false_positive_details: typing.Optional[FalsePositiveDetails] = pydantic.Field(alias="falsePositiveDetails")
    sanctions_details: typing.Optional[typing.List[SanctionsDetails]] = pydantic.Field(alias="sanctionsDetails")

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
