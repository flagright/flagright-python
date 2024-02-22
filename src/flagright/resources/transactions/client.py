# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.forbidden_error import ForbiddenError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.boolean_string import BooleanString
from ...types.transaction import Transaction
from ...types.transaction_with_rules_result import TransactionWithRulesResult
from .types.transactions_verify_response import TransactionsVerifyResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def verify(
        self,
        *,
        validate_origin_user_id: typing.Optional[BooleanString] = None,
        validate_destination_user_id: typing.Optional[BooleanString] = None,
        request: Transaction,
    ) -> TransactionsVerifyResponse:
        """
        ## POST Transactions

        `/transactions` endpoint allows you to operate on the [Transaction entity.](/guides/overview/entities#transaction)

        In order to pass the payload of a transaction to Flagright and verify the transaction, you will need to call this endpoint with the transaction payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Here are some of the most used payload fields explained (you can find the full payload [schema below](/api-reference/api-reference/transactions/verify#request) with 1 line descriptions):

        - `type`: Type of transaction (Ex: `WITHDRAWAL`, `DEPOSIT`, `TRANSFER` etc).
        - `transactionId` - Unique Identifier for the transaction. Flagright API will generate a `transactionId` if this field is left empty
        - `timestamp` - UNIX timestamp in _milliseconds_ of when the transaction took place
        - `transactionState` - The state of the transaction, set to `CREATED` by default. [More details here](/guides/overview/entities#transaction-lifecycle-through-transaction-events)
        - `originUserId` - Unique identifier (if any) of the user who is sending the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
        - `destinationUserId` - Unique identifier (if any) of the user who is receiving the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
        - `originAmountDetails` - Details of the amount being sent from the origin
        - `destinationAmountDetails` - Details of the amount being received at the destination
        - `originPaymentDetails` - Payment details (if any) used at the origin (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
        - `destinationPaymentDetails` - Payment details (if any) used at the destination (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.

        Parameters:
            - validate_origin_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided originUserId exist. True by default

            - validate_destination_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided destinationUserId exist. True by default

            - request: Transaction.
        ---
        from flagright import (
            CountryCode,
            CurrencyCode,
            DeviceData,
            Tag,
            Transaction,
            TransactionAmountDetails,
            TransactionType,
        )
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.transactions.verify(
            request=Transaction(
                origin_amount_details=TransactionAmountDetails(
                    transaction_amount=800.0,
                    transaction_currency=CurrencyCode.EUR,
                    country=CountryCode.DE,
                ),
                destination_amount_details=TransactionAmountDetails(
                    transaction_amount=68351.34,
                    transaction_currency=CurrencyCode.INR,
                    country=CountryCode.IN,
                ),
                promotion_code_used=True,
                reference="loan repayment",
                origin_device_data=DeviceData(
                    battery_level=95.0,
                    device_latitude=13.0033,
                    device_longitude=76.1004,
                    ip_address="10.23.191.2",
                    device_identifier="3c49f915d04485e34caba",
                    vpn_used=False,
                    operating_system="Android 11.2",
                    device_maker="ASUS",
                    device_model="Zenphone M2 Pro Max",
                    device_year="2018",
                    app_version="1.1.0",
                ),
                destination_device_data=DeviceData(
                    battery_level=95.0,
                    device_latitude=13.0033,
                    device_longitude=76.1004,
                    ip_address="10.23.191.2",
                    device_identifier="3c49f915d04485e34caba",
                    vpn_used=False,
                    operating_system="Android 11.2",
                    device_maker="ASUS",
                    device_model="Zenphone M2 Pro Max",
                    device_year="2018",
                    app_version="1.1.0",
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
                type=TransactionType.DEPOSIT,
                transaction_id="7b80a539eea6e78acbd6d458e5971482",
                timestamp=1641654664000.0,
                origin_user_id="8650a2611d0771cba03310f74bf6",
                destination_user_id="9350a2611e0771cba03310f74bf6",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "transactions"),
            params=remove_none_from_dict(
                {
                    "validateOriginUserId": validate_origin_user_id,
                    "validateDestinationUserId": validate_destination_user_id,
                }
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionsVerifyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, transaction_id: str) -> TransactionWithRulesResult:
        """
        ### GET Transactions

        `/transactions` endpoint allows you to operate on the [Transaction entity](/guides/overview/entities#transaction).

        Calling `GET /transactions/{transactionId}` will return the entire transaction payload and rule execution results for the transaction with the corresponding `transactionId`

        Parameters:
            - transaction_id: str. Unique Transaction Identifier
        ---
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.transactions.get(
            transaction_id="transactionId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"transactions/{transaction_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionWithRulesResult, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def verify(
        self,
        *,
        validate_origin_user_id: typing.Optional[BooleanString] = None,
        validate_destination_user_id: typing.Optional[BooleanString] = None,
        request: Transaction,
    ) -> TransactionsVerifyResponse:
        """
        ## POST Transactions

        `/transactions` endpoint allows you to operate on the [Transaction entity.](/guides/overview/entities#transaction)

        In order to pass the payload of a transaction to Flagright and verify the transaction, you will need to call this endpoint with the transaction payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Here are some of the most used payload fields explained (you can find the full payload [schema below](/api-reference/api-reference/transactions/verify#request) with 1 line descriptions):

        - `type`: Type of transaction (Ex: `WITHDRAWAL`, `DEPOSIT`, `TRANSFER` etc).
        - `transactionId` - Unique Identifier for the transaction. Flagright API will generate a `transactionId` if this field is left empty
        - `timestamp` - UNIX timestamp in _milliseconds_ of when the transaction took place
        - `transactionState` - The state of the transaction, set to `CREATED` by default. [More details here](/guides/overview/entities#transaction-lifecycle-through-transaction-events)
        - `originUserId` - Unique identifier (if any) of the user who is sending the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
        - `destinationUserId` - Unique identifier (if any) of the user who is receiving the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
        - `originAmountDetails` - Details of the amount being sent from the origin
        - `destinationAmountDetails` - Details of the amount being received at the destination
        - `originPaymentDetails` - Payment details (if any) used at the origin (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
        - `destinationPaymentDetails` - Payment details (if any) used at the destination (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.

        Parameters:
            - validate_origin_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided originUserId exist. True by default

            - validate_destination_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided destinationUserId exist. True by default

            - request: Transaction.
        ---
        from flagright import (
            CountryCode,
            CurrencyCode,
            DeviceData,
            Tag,
            Transaction,
            TransactionAmountDetails,
            TransactionType,
        )
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.transactions.verify(
            request=Transaction(
                origin_amount_details=TransactionAmountDetails(
                    transaction_amount=800.0,
                    transaction_currency=CurrencyCode.EUR,
                    country=CountryCode.DE,
                ),
                destination_amount_details=TransactionAmountDetails(
                    transaction_amount=68351.34,
                    transaction_currency=CurrencyCode.INR,
                    country=CountryCode.IN,
                ),
                promotion_code_used=True,
                reference="loan repayment",
                origin_device_data=DeviceData(
                    battery_level=95.0,
                    device_latitude=13.0033,
                    device_longitude=76.1004,
                    ip_address="10.23.191.2",
                    device_identifier="3c49f915d04485e34caba",
                    vpn_used=False,
                    operating_system="Android 11.2",
                    device_maker="ASUS",
                    device_model="Zenphone M2 Pro Max",
                    device_year="2018",
                    app_version="1.1.0",
                ),
                destination_device_data=DeviceData(
                    battery_level=95.0,
                    device_latitude=13.0033,
                    device_longitude=76.1004,
                    ip_address="10.23.191.2",
                    device_identifier="3c49f915d04485e34caba",
                    vpn_used=False,
                    operating_system="Android 11.2",
                    device_maker="ASUS",
                    device_model="Zenphone M2 Pro Max",
                    device_year="2018",
                    app_version="1.1.0",
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
                type=TransactionType.DEPOSIT,
                transaction_id="7b80a539eea6e78acbd6d458e5971482",
                timestamp=1641654664000.0,
                origin_user_id="8650a2611d0771cba03310f74bf6",
                destination_user_id="9350a2611e0771cba03310f74bf6",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "transactions"),
            params=remove_none_from_dict(
                {
                    "validateOriginUserId": validate_origin_user_id,
                    "validateDestinationUserId": validate_destination_user_id,
                }
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionsVerifyResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, transaction_id: str) -> TransactionWithRulesResult:
        """
        ### GET Transactions

        `/transactions` endpoint allows you to operate on the [Transaction entity](/guides/overview/entities#transaction).

        Calling `GET /transactions/{transactionId}` will return the entire transaction payload and rule execution results for the transaction with the corresponding `transactionId`

        Parameters:
            - transaction_id: str. Unique Transaction Identifier
        ---
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.transactions.get(
            transaction_id="transactionId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"transactions/{transaction_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionWithRulesResult, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
