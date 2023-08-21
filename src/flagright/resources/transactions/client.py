# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.boolean_string import BooleanString
from ...types.transaction import Transaction
from ...types.transaction_with_rules_result import TransactionWithRulesResult
from ...types.transactions_verify_response import TransactionsVerifyResponse

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

        `/transactions` endpoint allows you to operate on the [Transaction entity.](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships#transaction)

        In order to pass the payload of a transaction to Flagright and verify the transaciton, you will need to call this endpoint with the transaction payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.


        ### Payload

        Here are some of the most used payload fields explained (you can find the full payload [schema below](https://docs.flagright.com/docs/flagright-api/87742ed31b30e-verify-a-transaction#request-body) with 1 line descriptions):

        * `type`: Type of transaction (Ex: `WITHDRAWAL`, `DEPOSIT`, `TRANSFER` etc).
        * `transactionId` - Unique Identifier for the transaction. Flagright API will generate a `transactionId` if this field is left empty
        * `timestamp` - UNIX timestamp in *milliseconds* of when the transaction took place
        * `transactionState` - The state of the transaction, set to `CREATED` by default. [More details here](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships-in-the-api#transaction-lifecycle-through-transaction-events)
        * `originUserId` - Unique identifier (if any) of the user who is sending the money. This user must be created within the Flagright system before using the [create a consumer user](https://docs.flagright.com/docs/flagright-api/18132cd454603-create-a-consumer-user) or [create a business user](https://docs.flagright.com/docs/flagright-api/f651463db29d8-create-a-business-user) endpoint
        * `destinationUserId` - Unique identifier (if any) of the user who is receiving the money. This user must be created within the Flagright system before using the [create a consumer user](https://docs.flagright.com/docs/flagright-api/18132cd454603-create-a-consumer-user) or [create a business user](https://docs.flagright.com/docs/flagright-api/f651463db29d8-create-a-business-user) endpoint
        * `originAmountDetails` - Details of the amount being sent from the origin
        * `destinationAmountDetails` - Details of the amount being received at the destination
        * `originPaymentDetails` - Payment details (if any) used at the origin (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
        * `destinationPaymentDetails` - Payment details (if any) used at the destination (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.

        Parameters:
            - validate_origin_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided originUserId exist. True by default

            - validate_destination_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided destinationUserId exist. True by default

            - request: Transaction.
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

        `/transactions` endpoint allows you to operate on the [Transaction entity](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships#transaction).

        Calling `GET /transactions/{transactionId}` will return the entire transaction payload and rule execution results for the transaction with the corresponding `transactionId`

        Parameters:
            - transaction_id: str. Unique Transaction Identifier
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

        `/transactions` endpoint allows you to operate on the [Transaction entity.](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships#transaction)

        In order to pass the payload of a transaction to Flagright and verify the transaciton, you will need to call this endpoint with the transaction payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.


        ### Payload

        Here are some of the most used payload fields explained (you can find the full payload [schema below](https://docs.flagright.com/docs/flagright-api/87742ed31b30e-verify-a-transaction#request-body) with 1 line descriptions):

        * `type`: Type of transaction (Ex: `WITHDRAWAL`, `DEPOSIT`, `TRANSFER` etc).
        * `transactionId` - Unique Identifier for the transaction. Flagright API will generate a `transactionId` if this field is left empty
        * `timestamp` - UNIX timestamp in *milliseconds* of when the transaction took place
        * `transactionState` - The state of the transaction, set to `CREATED` by default. [More details here](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships-in-the-api#transaction-lifecycle-through-transaction-events)
        * `originUserId` - Unique identifier (if any) of the user who is sending the money. This user must be created within the Flagright system before using the [create a consumer user](https://docs.flagright.com/docs/flagright-api/18132cd454603-create-a-consumer-user) or [create a business user](https://docs.flagright.com/docs/flagright-api/f651463db29d8-create-a-business-user) endpoint
        * `destinationUserId` - Unique identifier (if any) of the user who is receiving the money. This user must be created within the Flagright system before using the [create a consumer user](https://docs.flagright.com/docs/flagright-api/18132cd454603-create-a-consumer-user) or [create a business user](https://docs.flagright.com/docs/flagright-api/f651463db29d8-create-a-business-user) endpoint
        * `originAmountDetails` - Details of the amount being sent from the origin
        * `destinationAmountDetails` - Details of the amount being received at the destination
        * `originPaymentDetails` - Payment details (if any) used at the origin (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
        * `destinationPaymentDetails` - Payment details (if any) used at the destination (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.

        Parameters:
            - validate_origin_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided originUserId exist. True by default

            - validate_destination_user_id: typing.Optional[BooleanString]. Boolean string whether Flagright should validate if provided destinationUserId exist. True by default

            - request: Transaction.
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

        `/transactions` endpoint allows you to operate on the [Transaction entity](https://docs.flagright.com/docs/flagright-api/8c06ae6a3231a-entities-and-relationships#transaction).

        Calling `GET /transactions/{transactionId}` will return the entire transaction payload and rule execution results for the transaction with the corresponding `transactionId`

        Parameters:
            - transaction_id: str. Unique Transaction Identifier
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
