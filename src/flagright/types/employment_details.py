# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EmploymentDetails(UniversalBaseModel):
    """
    Details of User's employment
    """

    employment_sector: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="employmentSector")] = (
        pydantic.Field(default=None)
    )
    """
    Sector of employment
    """

    employer_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="employerName")] = (
        pydantic.Field(default=None)
    )
    """
    Name of the employer
    """

    business_industry: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="businessIndustry")
    ] = pydantic.Field(default=None)
    """
    The industry in which the business operates for a business customer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
