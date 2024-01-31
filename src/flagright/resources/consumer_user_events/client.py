# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.boolean_string import BooleanString
from ...types.user_optional import UserOptional
from ...types.user_with_rules_result import UserWithRulesResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConsumerUserEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        allow_user_type_conversion: typing.Optional[BooleanString] = None,
        timestamp: float,
        user_id: str,
        event_id: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        event_description: typing.Optional[str] = OMIT,
        updated_consumer_user_attributes: typing.Optional[UserOptional] = OMIT,
    ) -> UserWithRulesResult:
        """
        ## POST Consumer User Events

        `/events/consumer/user` endpoint allows you to operate on the Consumer User Events entity.

        User events are created after the initial `POST /consumer/users` call (which creates a user) and are used to:

        - Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
        - Update the user details, using the `updatedConsumerUserAttributes` field.

        > If you have neither of the above two use cases, you do not need to use user events.

        ### Payload

        Each user event needs three mandatory fields:

        - `timestamp`- the timestamp of when the event was created or occured in your system
        - `userId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters:
            - allow_user_type_conversion: typing.Optional[BooleanString]. Boolean string whether Flagright should allow a Consumer user event to be applied to a Business user with the same user ID. This will converts a Business user to a Consumer user.

            - timestamp: float. Timestamp of the event

            - user_id: str. Transaction ID the event pertains to

            - event_id: typing.Optional[str]. Unique event ID

            - reason: typing.Optional[str]. Reason for the event or a state change

            - event_description: typing.Optional[str]. Event description

            - updated_consumer_user_attributes: typing.Optional[UserOptional].
        ---
        from flagright import (AcquisitionChannel, Address, Amount, BooleanString,
                               ConsumerName, ConsumerUserSegment, ContactDetails,
                               CountryCode, CurrencyCode, EmploymentStatus, Gender,
                               KycStatus, KycStatusDetails, LegalDocument, PepStatus,
                               RiskLevel, SourceOfFunds, Tag, TransactionAmountLimit,
                               TransactionCountLimit, TransactionLimit,
                               TransactionLimits, TransactionLimitsPaymentMethodLimits,
                               UserDetails, UserOptional, UserState, UserStateDetails)
        from flagright.client import Flagright

        client = Flagright(api_key="YOUR_API_KEY", )
        client.consumer_user_events.create(allow_user_type_conversion=BooleanString.TRUE, timestamp=1.1, user_id="string", updated_consumer_user_attributes=UserOptional(user_details=UserDetails(name=ConsumerName(first_name="string", ), country_of_residence=CountryCode.AF, country_of_nationality=CountryCode.AF, gender=Gender.M, ), user_state_details=UserStateDetails(state=UserState.UNACCEPTABLE, ), kyc_status_details=KycStatusDetails(status=KycStatus.SUCCESSFUL, ), employment_status=EmploymentStatus.UNEMPLOYED, legal_documents=[LegalDocument(document_type="string", document_number="string", document_issued_country=CountryCode.AF, tags=[Tag(key="string", value="string", )], name_on_document=ConsumerName(first_name="string", ), )], contact_details=ContactDetails(addresses=[Address(address_lines=[], city="string", country="string", tags=[Tag(key="string", value="string", )], )], ), transaction_limits=TransactionLimits(maximum_daily_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_weekly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_monthly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_quarterly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_yearly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), payment_method_limits=TransactionLimitsPaymentMethodLimits(ach=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), card=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), iban=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), upi=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), generic_bank_account=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), mpesa=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), swift=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), wallet=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), check=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), ), ), risk_level=RiskLevel.VERY_HIGH, acquisition_channel=AcquisitionChannel.ORGANIC, source_of_funds=[SourceOfFunds.EARNINGS], user_segment=ConsumerUserSegment.RETAIL, pep_status=[PepStatus(is_pep_hit=True, )], tags=[Tag(key="string", value="string", )], ), )
        """
        _request: typing.Dict[str, typing.Any] = {"timestamp": timestamp, "userId": user_id}
        if event_id is not OMIT:
            _request["eventId"] = event_id
        if reason is not OMIT:
            _request["reason"] = reason
        if event_description is not OMIT:
            _request["eventDescription"] = event_description
        if updated_consumer_user_attributes is not OMIT:
            _request["updatedConsumerUserAttributes"] = updated_consumer_user_attributes
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/consumer/user"),
            params=remove_none_from_dict({"allowUserTypeConversion": allow_user_type_conversion}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserWithRulesResult, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncConsumerUserEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        allow_user_type_conversion: typing.Optional[BooleanString] = None,
        timestamp: float,
        user_id: str,
        event_id: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        event_description: typing.Optional[str] = OMIT,
        updated_consumer_user_attributes: typing.Optional[UserOptional] = OMIT,
    ) -> UserWithRulesResult:
        """
        ## POST Consumer User Events

        `/events/consumer/user` endpoint allows you to operate on the Consumer User Events entity.

        User events are created after the initial `POST /consumer/users` call (which creates a user) and are used to:

        - Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
        - Update the user details, using the `updatedConsumerUserAttributes` field.

        > If you have neither of the above two use cases, you do not need to use user events.

        ### Payload

        Each user event needs three mandatory fields:

        - `timestamp`- the timestamp of when the event was created or occured in your system
        - `userId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters:
            - allow_user_type_conversion: typing.Optional[BooleanString]. Boolean string whether Flagright should allow a Consumer user event to be applied to a Business user with the same user ID. This will converts a Business user to a Consumer user.

            - timestamp: float. Timestamp of the event

            - user_id: str. Transaction ID the event pertains to

            - event_id: typing.Optional[str]. Unique event ID

            - reason: typing.Optional[str]. Reason for the event or a state change

            - event_description: typing.Optional[str]. Event description

            - updated_consumer_user_attributes: typing.Optional[UserOptional].
        ---
        from flagright import (AcquisitionChannel, Address, Amount, BooleanString,
                               ConsumerName, ConsumerUserSegment, ContactDetails,
                               CountryCode, CurrencyCode, EmploymentStatus, Gender,
                               KycStatus, KycStatusDetails, LegalDocument, PepStatus,
                               RiskLevel, SourceOfFunds, Tag, TransactionAmountLimit,
                               TransactionCountLimit, TransactionLimit,
                               TransactionLimits, TransactionLimitsPaymentMethodLimits,
                               UserDetails, UserOptional, UserState, UserStateDetails)
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(api_key="YOUR_API_KEY", )
        await client.consumer_user_events.create(allow_user_type_conversion=BooleanString.TRUE, timestamp=1.1, user_id="string", updated_consumer_user_attributes=UserOptional(user_details=UserDetails(name=ConsumerName(first_name="string", ), country_of_residence=CountryCode.AF, country_of_nationality=CountryCode.AF, gender=Gender.M, ), user_state_details=UserStateDetails(state=UserState.UNACCEPTABLE, ), kyc_status_details=KycStatusDetails(status=KycStatus.SUCCESSFUL, ), employment_status=EmploymentStatus.UNEMPLOYED, legal_documents=[LegalDocument(document_type="string", document_number="string", document_issued_country=CountryCode.AF, tags=[Tag(key="string", value="string", )], name_on_document=ConsumerName(first_name="string", ), )], contact_details=ContactDetails(addresses=[Address(address_lines=[], city="string", country="string", tags=[Tag(key="string", value="string", )], )], ), transaction_limits=TransactionLimits(maximum_daily_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_weekly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_monthly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_quarterly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), maximum_yearly_transaction_limit=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), payment_method_limits=TransactionLimitsPaymentMethodLimits(ach=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), card=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), iban=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), upi=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), generic_bank_account=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), mpesa=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), swift=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), wallet=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), check=TransactionLimit(transaction_count_limit=TransactionCountLimit(), transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), average_transaction_amount_limit=TransactionAmountLimit(day=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), week=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), month=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), year=Amount(amount_value=1.1, amount_currency=CurrencyCode.1_INCH, ), ), ), ), ), risk_level=RiskLevel.VERY_HIGH, acquisition_channel=AcquisitionChannel.ORGANIC, source_of_funds=[SourceOfFunds.EARNINGS], user_segment=ConsumerUserSegment.RETAIL, pep_status=[PepStatus(is_pep_hit=True, )], tags=[Tag(key="string", value="string", )], ), )
        """
        _request: typing.Dict[str, typing.Any] = {"timestamp": timestamp, "userId": user_id}
        if event_id is not OMIT:
            _request["eventId"] = event_id
        if reason is not OMIT:
            _request["reason"] = reason
        if event_description is not OMIT:
            _request["eventDescription"] = event_description
        if updated_consumer_user_attributes is not OMIT:
            _request["updatedConsumerUserAttributes"] = updated_consumer_user_attributes
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/consumer/user"),
            params=remove_none_from_dict({"allowUserTypeConversion": allow_user_type_conversion}),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserWithRulesResult, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
