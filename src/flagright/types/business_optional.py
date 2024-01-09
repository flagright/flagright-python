# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .acquisition_channel import AcquisitionChannel
from .business_entity_link import BusinessEntityLink
from .business_optional_saved_payment_details_item import BusinessOptionalSavedPaymentDetailsItem
from .kyc_status_details import KycStatusDetails
from .legal_entity import LegalEntity
from .mcc_details import MccDetails
from .payment_method import PaymentMethod
from .person import Person
from .risk_level import RiskLevel
from .tag import Tag
from .transaction_limits import TransactionLimits
from .user_state_details import UserStateDetails

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BusinessOptional(pydantic.BaseModel):
    """
    Model for a business user - optional fields
    """

    user_state_details: typing.Optional[UserStateDetails] = pydantic.Field(alias="userStateDetails")
    kyc_status_details: typing.Optional[KycStatusDetails] = pydantic.Field(alias="kycStatusDetails")
    legal_entity: typing.Optional[LegalEntity] = pydantic.Field(alias="legalEntity")
    share_holders: typing.Optional[typing.List[Person]] = pydantic.Field(
        alias="shareHolders",
        description="Shareholders (beneficiaries) of the company that hold at least 25% ownership. Can be another company or an individual",
    )
    directors: typing.Optional[typing.List[Person]] = pydantic.Field(
        description="Director(s) of the company. Must be at least one"
    )
    transaction_limits: typing.Optional[TransactionLimits] = pydantic.Field(alias="transactionLimits")
    risk_level: typing.Optional[RiskLevel] = pydantic.Field(alias="riskLevel")
    allowed_payment_methods: typing.Optional[typing.List[PaymentMethod]] = pydantic.Field(alias="allowedPaymentMethods")
    linked_entities: typing.Optional[BusinessEntityLink] = pydantic.Field(alias="linkedEntities")
    acquisition_channel: typing.Optional[AcquisitionChannel] = pydantic.Field(alias="acquisitionChannel")
    saved_payment_details: typing.Optional[typing.List[BusinessOptionalSavedPaymentDetailsItem]] = pydantic.Field(
        alias="savedPaymentDetails"
    )
    mcc_details: typing.Optional[MccDetails] = pydantic.Field(alias="mccDetails")
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(
        description="Additional information that can be added via tags"
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
