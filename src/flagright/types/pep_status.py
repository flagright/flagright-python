# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import typing
from .country_code import CountryCode
from .pep_rank import PepRank
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PepStatus(UniversalBaseModel):
    is_pep_hit: typing_extensions.Annotated[bool, FieldMetadata(alias="isPepHit")]
    pep_country: typing_extensions.Annotated[typing.Optional[CountryCode], FieldMetadata(alias="pepCountry")] = None
    pep_rank: typing_extensions.Annotated[typing.Optional[PepRank], FieldMetadata(alias="pepRank")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
