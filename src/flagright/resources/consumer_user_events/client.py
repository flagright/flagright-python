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
from ...types.consumer_user_event import ConsumerUserEvent
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
        self, *, allow_user_type_conversion: typing.Optional[BooleanString] = None, request: ConsumerUserEvent
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

            - request: ConsumerUserEvent.
        ---
        from flagright import ConsumerUserEvent
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_user_events.create(
            request=ConsumerUserEvent(
                timestamp=1.1,
                user_id="userId",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/consumer/user"),
            params=remove_none_from_dict({"allowUserTypeConversion": allow_user_type_conversion}),
            json=jsonable_encoder(request),
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

    def get(self, event_id: str) -> ConsumerUserEvent:
        """
        ### GET a Consumer User Event

        You can retrieve any consumer user event you created using the [POST Consumer User Events](/api-reference/api-reference/consumer-user-events/create) call.

        Parameters:
            - event_id: str. Unique Consumer User Event Identifier
        ---
        from flagright.client import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_user_events.get(
            event_id="eventId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/consumer/user/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConsumerUserEvent, _response.json())  # type: ignore
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
        self, *, allow_user_type_conversion: typing.Optional[BooleanString] = None, request: ConsumerUserEvent
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

            - request: ConsumerUserEvent.
        ---
        from flagright import ConsumerUserEvent
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.consumer_user_events.create(
            request=ConsumerUserEvent(
                timestamp=1.1,
                user_id="userId",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "events/consumer/user"),
            params=remove_none_from_dict({"allowUserTypeConversion": allow_user_type_conversion}),
            json=jsonable_encoder(request),
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

    async def get(self, event_id: str) -> ConsumerUserEvent:
        """
        ### GET a Consumer User Event

        You can retrieve any consumer user event you created using the [POST Consumer User Events](/api-reference/api-reference/consumer-user-events/create) call.

        Parameters:
            - event_id: str. Unique Consumer User Event Identifier
        ---
        from flagright.client import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )
        await client.consumer_user_events.get(
            event_id="eventId",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"events/consumer/user/{event_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ConsumerUserEvent, _response.json())  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
