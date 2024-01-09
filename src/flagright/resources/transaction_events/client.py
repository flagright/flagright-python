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
from ...types.transaction_event import TransactionEvent
from ...types.transaction_event_monitoring_result import TransactionEventMonitoringResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TransactionEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: TransactionEvent) -> TransactionEventMonitoringResult:
        """
        ## POST Transaction Events

        `/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-event)

        Transaction events are created after the initial `POST /transactions` call (which creates a transaction) and are used to:

        - Update the STATE of the transaction, using the `transactionState` field and manage the [Transaction Lifecycle](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-lifecycle-through-transaction-events)
        - Update the transaction details, using the `updatedTransactionAttributes` field.

        > If you have neither of the above two use cases, you do not need to use transaction events.

        ### Payload

        Each transaction event needs three mandatory fields:

        - `transactionState` - STATE of the transaction -> value is set to `CREATED` after `POST /transactions` call
        - `timestamp`- the timestamp of when the event was created or occured in your system
        - `transactionId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters:
            - request: TransactionEvent.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/transaction"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionEventMonitoringResult, _response.json())  # type: ignore
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

    def get(self, event_id: str) -> TransactionEvent:
        """
        ### GET Transaction Events

        `/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-event).

        You can retrieve any transaction event you create using the [POST Transaction Events](https://docs.flagright.com/docs/flagright-api/d7c4dc4d02850-create-a-transaction-event) call.

        Parameters:
            - event_id: str. Unique Transaction Identifier
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/transaction/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionEvent, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTransactionEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, request: TransactionEvent) -> TransactionEventMonitoringResult:
        """
        ## POST Transaction Events

        `/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-event)

        Transaction events are created after the initial `POST /transactions` call (which creates a transaction) and are used to:

        - Update the STATE of the transaction, using the `transactionState` field and manage the [Transaction Lifecycle](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-lifecycle-through-transaction-events)
        - Update the transaction details, using the `updatedTransactionAttributes` field.

        > If you have neither of the above two use cases, you do not need to use transaction events.

        ### Payload

        Each transaction event needs three mandatory fields:

        - `transactionState` - STATE of the transaction -> value is set to `CREATED` after `POST /transactions` call
        - `timestamp`- the timestamp of when the event was created or occured in your system
        - `transactionId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters:
            - request: TransactionEvent.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/transaction"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionEventMonitoringResult, _response.json())  # type: ignore
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

    async def get(self, event_id: str) -> TransactionEvent:
        """
        ### GET Transaction Events

        `/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#transaction-event).

        You can retrieve any transaction event you create using the [POST Transaction Events](https://docs.flagright.com/docs/flagright-api/d7c4dc4d02850-create-a-transaction-event) call.

        Parameters:
            - event_id: str. Unique Transaction Identifier
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/transaction/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TransactionEvent, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
