# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .country_code import CountryCode

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class DeviceData(pydantic.BaseModel):
    """
    Model for device data
    """

    battery_level: typing.Optional[float] = pydantic.Field(
        alias="batteryLevel",
        description="Battery level of the device used for a transaction or event at a given timestamp",
    )
    device_latitude: typing.Optional[float] = pydantic.Field(
        alias="deviceLatitude", description="Device latitude at a give timestamp for an event or transaction"
    )
    device_longitude: typing.Optional[float] = pydantic.Field(
        alias="deviceLongitude", description="Device longitude at a give timestamp for an event or transaction"
    )
    ip_address: typing.Optional[str] = pydantic.Field(
        alias="ipAddress", description="IP address of the device at a given timestamp for an event or transaction"
    )
    ip_country: typing.Optional[CountryCode] = pydantic.Field(alias="ipCountry")
    device_identifier: typing.Optional[str] = pydantic.Field(
        alias="deviceIdentifier", description="Device identifier number"
    )
    vpn_used: typing.Optional[bool] = pydantic.Field(
        alias="vpnUsed", description="Whether VPN was used at a given timestamp for an event or transaction"
    )
    operating_system: typing.Optional[str] = pydantic.Field(
        alias="operatingSystem",
        description="Operating system of the device at a given timestamp for an event or transaction",
    )
    device_maker: typing.Optional[str] = pydantic.Field(
        alias="deviceMaker", description="The maker of the device at a given timestamp for an event or transaction"
    )
    device_model: typing.Optional[str] = pydantic.Field(
        alias="deviceModel", description="The model of the device at a given timestamp for an event or transaction"
    )
    device_year: typing.Optional[str] = pydantic.Field(
        alias="deviceYear",
        description="The year the device was manufactured at a given timestamp for an event or transaction",
    )
    app_version: typing.Optional[str] = pydantic.Field(
        alias="appVersion",
        description="The version of the app your user is using on their device at a given timestamp for an event or transaction",
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
