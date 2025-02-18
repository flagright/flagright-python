# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .acquisition_channel import AcquisitionChannel
from .consumer_user_segment import ConsumerUserSegment
from .contact_details import ContactDetails
from .employment_details import EmploymentDetails
from .employment_status import EmploymentStatus
from .expected_income import ExpectedIncome
from .kyc_status_details import KycStatusDetails
from .legal_document import LegalDocument
from .pep_status import PepStatus
from .person_attachment import PersonAttachment
from .risk_level import RiskLevel
from .source_of_funds import SourceOfFunds
from .transaction_limits import TransactionLimits
from .user_details import UserDetails
from .user_entity_link import UserEntityLink
from .user_optional_saved_payment_details_item import UserOptionalSavedPaymentDetailsItem
from .user_state_details import UserStateDetails
from .user_tag import UserTag

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UserOptional(pydantic.BaseModel):
    """
    Model for User details
    """

    activated_timestamp: typing.Optional[float] = pydantic.Field(
        alias="activatedTimestamp", description="Timestamp when user was activated"
    )
    user_details: typing.Optional[UserDetails] = pydantic.Field(alias="userDetails")
    user_state_details: typing.Optional[UserStateDetails] = pydantic.Field(alias="userStateDetails")
    kyc_status_details: typing.Optional[KycStatusDetails] = pydantic.Field(alias="kycStatusDetails")
    employment_status: typing.Optional[EmploymentStatus] = pydantic.Field(alias="employmentStatus")
    occupation: typing.Optional[str]
    legal_documents: typing.Optional[typing.List[LegalDocument]] = pydantic.Field(
        alias="legalDocuments", description="User's legal identity documents - See Document Model for details"
    )
    contact_details: typing.Optional[ContactDetails] = pydantic.Field(alias="contactDetails")
    employment_details: typing.Optional[EmploymentDetails] = pydantic.Field(alias="employmentDetails")
    transaction_limits: typing.Optional[TransactionLimits] = pydantic.Field(alias="transactionLimits")
    expected_income: typing.Optional[ExpectedIncome] = pydantic.Field(alias="expectedIncome")
    risk_level: typing.Optional[RiskLevel] = pydantic.Field(alias="riskLevel")
    kyc_risk_level: typing.Optional[RiskLevel] = pydantic.Field(alias="kycRiskLevel")
    acquisition_channel: typing.Optional[AcquisitionChannel] = pydantic.Field(alias="acquisitionChannel")
    reason_for_account_opening: typing.Optional[typing.List[str]] = pydantic.Field(alias="reasonForAccountOpening")
    source_of_funds: typing.Optional[typing.List[SourceOfFunds]] = pydantic.Field(alias="sourceOfFunds")
    user_segment: typing.Optional[ConsumerUserSegment] = pydantic.Field(alias="userSegment")
    pep_status: typing.Optional[typing.List[PepStatus]] = pydantic.Field(alias="pepStatus")
    last_transaction_timestamp: typing.Optional[float] = pydantic.Field(
        alias="lastTransactionTimestamp", description="Timestamp of the last successful transaction of the user"
    )
    linked_entities: typing.Optional[UserEntityLink] = pydantic.Field(alias="linkedEntities")
    saved_payment_details: typing.Optional[typing.List[UserOptionalSavedPaymentDetailsItem]] = pydantic.Field(
        alias="savedPaymentDetails"
    )
    tags: typing.Optional[typing.List[UserTag]] = pydantic.Field(
        description="Additional information that can be added via tags"
    )
    attachments: typing.Optional[typing.List[PersonAttachment]] = pydantic.Field(
        description="Uploaded user's attachment"
    )

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
