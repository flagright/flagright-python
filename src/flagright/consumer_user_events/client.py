# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .raw_client import RawConsumerUserEventsClient
from ..types.boolean_string import BooleanString
from ..types.user_optional import UserOptional
from ..core.request_options import RequestOptions
from ..types.user_with_rules_result import UserWithRulesResult
from ..types.consumer_user_event_with_rules_result import ConsumerUserEventWithRulesResult
from ..core.client_wrapper import AsyncClientWrapper
from .raw_client import AsyncRawConsumerUserEventsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ConsumerUserEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConsumerUserEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConsumerUserEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConsumerUserEventsClient
        """
        return self._raw_client

    def create(
        self,
        *,
        timestamp: float,
        user_id: str,
        allow_user_type_conversion: typing.Optional[BooleanString] = None,
        lock_kyc_risk_level: typing.Optional[BooleanString] = None,
        lock_cra_risk_level: typing.Optional[BooleanString] = None,
        event_id: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        event_description: typing.Optional[str] = OMIT,
        updated_consumer_user_attributes: typing.Optional[UserOptional] = OMIT,
        update_count: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserWithRulesResult:
        """
        ## POST Consumer User Events

        `/events/consumer/user` endpoint allows you to operate on the Consumer User Events entity.

        User events are created after the initial `POST /consumer/users` call (which creates a user) and are used to:

        * Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
        * Update the user details, using the `updatedConsumerUserAttributes` field.

        > If you have neither of the above two use cases, you do not need to use user events.

        ### Payload

        Each user event needs three mandatory fields:

        * `timestamp`- the timestamp of when the event was created or occured in your system
        * `userId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters
        ----------
        timestamp : float
            Timestamp of the event

        user_id : str
            Transaction ID the event pertains to

        allow_user_type_conversion : typing.Optional[BooleanString]
            Boolean string whether Flagright should allow a Consumer user event to be applied to a Business user with the same user ID. This will converts a Business user to a Consumer user.

        lock_kyc_risk_level : typing.Optional[BooleanString]
            Boolean string whether Flagright should lock the KYC risk level for the user.

        lock_cra_risk_level : typing.Optional[BooleanString]
            Boolean string whether Flagright should lock the CRA risk level for the user.

        event_id : typing.Optional[str]
            Unique event ID

        reason : typing.Optional[str]
            Reason for the event or a state change

        event_description : typing.Optional[str]
            Event description

        updated_consumer_user_attributes : typing.Optional[UserOptional]

        update_count : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserWithRulesResult
            Created

        Examples
        --------
        from flagright import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_user_events.create(
            timestamp=1.1,
            user_id="userId",
        )
        """
        response = self._raw_client.create(
            timestamp=timestamp,
            user_id=user_id,
            allow_user_type_conversion=allow_user_type_conversion,
            lock_kyc_risk_level=lock_kyc_risk_level,
            lock_cra_risk_level=lock_cra_risk_level,
            event_id=event_id,
            reason=reason,
            event_description=event_description,
            updated_consumer_user_attributes=updated_consumer_user_attributes,
            update_count=update_count,
            request_options=request_options,
        )
        return response.data

    def get(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsumerUserEventWithRulesResult:
        """
        ### GET a Consumer User Event
        You can retrieve any consumer user event you created using the [POST Consumer User Events](/api-reference/api-reference/consumer-user-events/create) call.

        Parameters
        ----------
        event_id : str
            Unique Consumer User Event Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumerUserEventWithRulesResult
            OK

        Examples
        --------
        from flagright import Flagright

        client = Flagright(
            api_key="YOUR_API_KEY",
        )
        client.consumer_user_events.get(
            event_id="eventId",
        )
        """
        response = self._raw_client.get(event_id, request_options=request_options)
        return response.data


class AsyncConsumerUserEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConsumerUserEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConsumerUserEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConsumerUserEventsClient
        """
        return self._raw_client

    async def create(
        self,
        *,
        timestamp: float,
        user_id: str,
        allow_user_type_conversion: typing.Optional[BooleanString] = None,
        lock_kyc_risk_level: typing.Optional[BooleanString] = None,
        lock_cra_risk_level: typing.Optional[BooleanString] = None,
        event_id: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        event_description: typing.Optional[str] = OMIT,
        updated_consumer_user_attributes: typing.Optional[UserOptional] = OMIT,
        update_count: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserWithRulesResult:
        """
        ## POST Consumer User Events

        `/events/consumer/user` endpoint allows you to operate on the Consumer User Events entity.

        User events are created after the initial `POST /consumer/users` call (which creates a user) and are used to:

        * Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
        * Update the user details, using the `updatedConsumerUserAttributes` field.

        > If you have neither of the above two use cases, you do not need to use user events.

        ### Payload

        Each user event needs three mandatory fields:

        * `timestamp`- the timestamp of when the event was created or occured in your system
        * `userId` - The ID of the transaction for which this event is generated.

        In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.

        Parameters
        ----------
        timestamp : float
            Timestamp of the event

        user_id : str
            Transaction ID the event pertains to

        allow_user_type_conversion : typing.Optional[BooleanString]
            Boolean string whether Flagright should allow a Consumer user event to be applied to a Business user with the same user ID. This will converts a Business user to a Consumer user.

        lock_kyc_risk_level : typing.Optional[BooleanString]
            Boolean string whether Flagright should lock the KYC risk level for the user.

        lock_cra_risk_level : typing.Optional[BooleanString]
            Boolean string whether Flagright should lock the CRA risk level for the user.

        event_id : typing.Optional[str]
            Unique event ID

        reason : typing.Optional[str]
            Reason for the event or a state change

        event_description : typing.Optional[str]
            Event description

        updated_consumer_user_attributes : typing.Optional[UserOptional]

        update_count : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserWithRulesResult
            Created

        Examples
        --------
        import asyncio

        from flagright import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumer_user_events.create(
                timestamp=1.1,
                user_id="userId",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.create(
            timestamp=timestamp,
            user_id=user_id,
            allow_user_type_conversion=allow_user_type_conversion,
            lock_kyc_risk_level=lock_kyc_risk_level,
            lock_cra_risk_level=lock_cra_risk_level,
            event_id=event_id,
            reason=reason,
            event_description=event_description,
            updated_consumer_user_attributes=updated_consumer_user_attributes,
            update_count=update_count,
            request_options=request_options,
        )
        return response.data

    async def get(
        self, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConsumerUserEventWithRulesResult:
        """
        ### GET a Consumer User Event
        You can retrieve any consumer user event you created using the [POST Consumer User Events](/api-reference/api-reference/consumer-user-events/create) call.

        Parameters
        ----------
        event_id : str
            Unique Consumer User Event Identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConsumerUserEventWithRulesResult
            OK

        Examples
        --------
        import asyncio

        from flagright import AsyncFlagright

        client = AsyncFlagright(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consumer_user_events.get(
                event_id="eventId",
            )


        asyncio.run(main())
        """
        response = await self._raw_client.get(event_id, request_options=request_options)
        return response.data
