# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .hit_rules_details import HitRulesDetails
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class HitRulesResults(UniversalBaseModel):
    hit_rules: typing_extensions.Annotated[typing.List[HitRulesDetails], FieldMetadata(alias="hitRules")] = (
        pydantic.Field()
    )
    """
    Uniquue transaction identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
