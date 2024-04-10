# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .user_optional import UserOptional

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ConsumerUserEvent(pydantic.BaseModel):
    """
    Model for consumer user-related events
    """

    timestamp: float = pydantic.Field(description="Timestamp of the event")
    user_id: str = pydantic.Field(alias="userId", description="Transaction ID the event pertains to")
    event_id: typing.Optional[str] = pydantic.Field(alias="eventId", description="Unique event ID")
    reason: typing.Optional[str] = pydantic.Field(description="Reason for the event or a state change")
    event_description: typing.Optional[str] = pydantic.Field(alias="eventDescription", description="Event description")
    updated_consumer_user_attributes: typing.Optional[UserOptional] = pydantic.Field(
        alias="updatedConsumerUserAttributes"
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
