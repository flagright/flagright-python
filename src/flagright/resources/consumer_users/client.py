# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.user import User
from ...types.user_response import UserResponse
from .types.consumer_users_create_response import ConsumerUsersCreateResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConsumerUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: User) -> ConsumerUsersCreateResponse:
        """
        ## POST Consumer User

        `/consumer/user` endpoint allows you to operate on the Consumer user entity.

        In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Each consumer User entity needs three mandatory fields:

        - `userId` - Unique identifier for the user
        - `createdTimestamp` - UNIX timestamp in _milliseconds_ for when the User is created in your system

        Parameters:
            - request: User.
        ---
        from flagright import (
            Address,
            Amount,
            ConsumerName,
            ContactDetails,
            CountryCode,
            CurrencyCode,
            LegalDocument,
            Tag,
            TransactionLimits,
            User,
            UserDetails,
        )
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_users.create(
            request=User(
                user_details=UserDetails(
                    name=ConsumerName(
                        first_name="Baran",
                        middle_name="Realblood",
                        last_name="Ozkan",
                    ),
                    date_of_birth="1991-01-01",
                    country_of_residence=CountryCode.US,
                    country_of_nationality=CountryCode.DE,
                ),
                legal_documents=[
                    LegalDocument(
                        document_type="passport",
                        document_number="Z9431P",
                        document_issued_date=1639939034000.0,
                        document_expiration_date=1839939034000.0,
                        document_issued_country=CountryCode.DE,
                        tags=[
                            Tag(
                                key="customerType",
                                value="wallet",
                            ),
                            Tag(
                                key="customKey",
                                value="customValue",
                            ),
                        ],
                        name_on_document=ConsumerName(
                            first_name="Baran",
                            middle_name="Realblood",
                            last_name="Ozkan",
                        ),
                    ),
                    LegalDocument(
                        document_type="passport",
                        document_number="Z9431P",
                        document_issued_date=1639939034000.0,
                        document_expiration_date=1839939034000.0,
                        document_issued_country=CountryCode.DE,
                        tags=[
                            Tag(
                                key="customerType",
                                value="wallet",
                            ),
                            Tag(
                                key="customKey",
                                value="customValue",
                            ),
                        ],
                        name_on_document=ConsumerName(
                            first_name="Baran",
                            middle_name="Realblood",
                            last_name="Ozkan",
                        ),
                    ),
                ],
                contact_details=ContactDetails(
                    email_ids=["baran@flagright.com", "emailIds"],
                    contact_numbers=["+37112345432", "contactNumbers"],
                    websites=["flagright.com", "websites"],
                    addresses=[
                        Address(
                            address_lines=["Klara-Franke Str 20"],
                            postcode="10557",
                            city="Berlin",
                            state="Berlin",
                            country="Germany",
                            tags=[
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                            ],
                        ),
                        Address(
                            address_lines=["Klara-Franke Str 20"],
                            postcode="10557",
                            city="Berlin",
                            state="Berlin",
                            country="Germany",
                            tags=[
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                            ],
                        ),
                    ],
                ),
                transaction_limits=TransactionLimits(
                    maximum_daily_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_weekly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_monthly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_quarterly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_yearly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                ),
                tags=[
                    Tag(
                        key="customKey",
                        value="customValue",
                    ),
                    Tag(
                        key="customKey",
                        value="customValue",
                    ),
                ],
                user_id="96647cfd9e8fe66ee0f3362e011e34e8",
                created_timestamp=1641654664000.0,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "consumer/users"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConsumerUsersCreateResponse, _response.json())  # type: ignore
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

    def get(self, user_id: str) -> UserResponse:
        """
        ### GET Consumer User

        `/consumer/user` endpoint allows you to operate on the Consumer User entity.

        Calling `GET /consumer/user/{userId}` will return the entire user payload and rule execution results for the user with the corresponding `userId`

        Parameters:
            - user_id: str.
        ---
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_users.get(
            user_id="userId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"consumer/users/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncConsumerUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, request: User) -> ConsumerUsersCreateResponse:
        """
        ## POST Consumer User

        `/consumer/user` endpoint allows you to operate on the Consumer user entity.

        In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Each consumer User entity needs three mandatory fields:

        - `userId` - Unique identifier for the user
        - `createdTimestamp` - UNIX timestamp in _milliseconds_ for when the User is created in your system

        Parameters:
            - request: User.
        ---
        from flagright import (
            Address,
            Amount,
            ConsumerName,
            ContactDetails,
            CountryCode,
            CurrencyCode,
            LegalDocument,
            Tag,
            TransactionLimits,
            User,
            UserDetails,
        )
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.consumer_users.create(
            request=User(
                user_details=UserDetails(
                    name=ConsumerName(
                        first_name="Baran",
                        middle_name="Realblood",
                        last_name="Ozkan",
                    ),
                    date_of_birth="1991-01-01",
                    country_of_residence=CountryCode.US,
                    country_of_nationality=CountryCode.DE,
                ),
                legal_documents=[
                    LegalDocument(
                        document_type="passport",
                        document_number="Z9431P",
                        document_issued_date=1639939034000.0,
                        document_expiration_date=1839939034000.0,
                        document_issued_country=CountryCode.DE,
                        tags=[
                            Tag(
                                key="customerType",
                                value="wallet",
                            ),
                            Tag(
                                key="customKey",
                                value="customValue",
                            ),
                        ],
                        name_on_document=ConsumerName(
                            first_name="Baran",
                            middle_name="Realblood",
                            last_name="Ozkan",
                        ),
                    ),
                    LegalDocument(
                        document_type="passport",
                        document_number="Z9431P",
                        document_issued_date=1639939034000.0,
                        document_expiration_date=1839939034000.0,
                        document_issued_country=CountryCode.DE,
                        tags=[
                            Tag(
                                key="customerType",
                                value="wallet",
                            ),
                            Tag(
                                key="customKey",
                                value="customValue",
                            ),
                        ],
                        name_on_document=ConsumerName(
                            first_name="Baran",
                            middle_name="Realblood",
                            last_name="Ozkan",
                        ),
                    ),
                ],
                contact_details=ContactDetails(
                    email_ids=["baran@flagright.com", "emailIds"],
                    contact_numbers=["+37112345432", "contactNumbers"],
                    websites=["flagright.com", "websites"],
                    addresses=[
                        Address(
                            address_lines=["Klara-Franke Str 20"],
                            postcode="10557",
                            city="Berlin",
                            state="Berlin",
                            country="Germany",
                            tags=[
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                            ],
                        ),
                        Address(
                            address_lines=["Klara-Franke Str 20"],
                            postcode="10557",
                            city="Berlin",
                            state="Berlin",
                            country="Germany",
                            tags=[
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                                Tag(
                                    key="customKey",
                                    value="customValue",
                                ),
                            ],
                        ),
                    ],
                ),
                transaction_limits=TransactionLimits(
                    maximum_daily_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_weekly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_monthly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_quarterly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                    maximum_yearly_transaction_limit=Amount(
                        amount_value=800.0,
                        amount_currency=CurrencyCode.GBP,
                    ),
                ),
                tags=[
                    Tag(
                        key="customKey",
                        value="customValue",
                    ),
                    Tag(
                        key="customKey",
                        value="customValue",
                    ),
                ],
                user_id="96647cfd9e8fe66ee0f3362e011e34e8",
                created_timestamp=1641654664000.0,
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "consumer/users"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConsumerUsersCreateResponse, _response.json())  # type: ignore
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

    async def get(self, user_id: str) -> UserResponse:
        """
        ### GET Consumer User

        `/consumer/user` endpoint allows you to operate on the Consumer User entity.

        Calling `GET /consumer/user/{userId}` will return the entire user payload and rule execution results for the user with the corresponding `userId`

        Parameters:
            - user_id: str.
        ---
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.consumer_users.get(
            user_id="userId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"consumer/users/{user_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UserResponse, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
