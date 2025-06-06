# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .rule_hit_direction import RuleHitDirection
from ..core.serialization import FieldMetadata
from .false_positive_details import FalsePositiveDetails
from .sanctions_details import SanctionsDetails
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RuleHitMeta(UniversalBaseModel):
    """
    Details of rule execution, for internal purposes only
    """

    hit_directions: typing_extensions.Annotated[
        typing.Optional[typing.List[RuleHitDirection]], FieldMetadata(alias="hitDirections")
    ] = None
    false_positive_details: typing_extensions.Annotated[
        typing.Optional[FalsePositiveDetails], FieldMetadata(alias="falsePositiveDetails")
    ] = None
    sanctions_details: typing_extensions.Annotated[
        typing.Optional[typing.List[SanctionsDetails]], FieldMetadata(alias="sanctionsDetails")
    ] = None
    is_ongoing_screening_hit: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isOngoingScreeningHit")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
