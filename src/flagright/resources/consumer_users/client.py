# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.consumer_users_create_response import ConsumerUsersCreateResponse
from ...types.user import User
from ...types.user_response import UserResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConsumerUsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: User) -> ConsumerUsersCreateResponse:
        """
        ## POST Consumer User

        `/consumer/user` endpoint allows you to operate on the [Consumer user entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#user)

        In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Each consumer User entity needs three mandatory fields:

        * `userId` - Unique identifier for the user
        * `createdTimestamp` - UNIX timestamp in *milliseconds* for when the User is created in your system

        Parameters:
            - request: User.
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

        `/consumer/user` endpoint allows you to operate on the [Consumer User entity](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#user).

        Calling `GET /consumer/user/{userId}` will return the entire user payload and rule execution results for the user with the corresponding `userId`

        Parameters:
            - user_id: str.
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

        `/consumer/user` endpoint allows you to operate on the [Consumer user entity.](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#user)

        In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

        ### Payload

        Each consumer User entity needs three mandatory fields:

        * `userId` - Unique identifier for the user
        * `createdTimestamp` - UNIX timestamp in *milliseconds* for when the User is created in your system

        Parameters:
            - request: User.
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

        `/consumer/user` endpoint allows you to operate on the [Consumer User entity](https://docs.flagright.com/docs/flagright-api/0f8fac59d1995-entities-and-relationships#user).

        Calling `GET /consumer/user/{userId}` will return the entire user payload and rule execution results for the user with the corresponding `userId`

        Parameters:
            - user_id: str.
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
