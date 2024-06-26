# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WebhookEventType(str, enum.Enum):
    CASE_CLOSED = "CASE_CLOSED"
    USER_STATE_UPDATED = "USER_STATE_UPDATED"
    ALERT_CLOSED = "ALERT_CLOSED"
    TRANSACTION_STATUS_UPDATED = "TRANSACTION_STATUS_UPDATED"
    KYC_STATUS_UPDATED = "KYC_STATUS_UPDATED"
    CASE_OPENED = "CASE_OPENED"
    ALERT_OPENED = "ALERT_OPENED"

    def visit(
        self,
        case_closed: typing.Callable[[], T_Result],
        user_state_updated: typing.Callable[[], T_Result],
        alert_closed: typing.Callable[[], T_Result],
        transaction_status_updated: typing.Callable[[], T_Result],
        kyc_status_updated: typing.Callable[[], T_Result],
        case_opened: typing.Callable[[], T_Result],
        alert_opened: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEventType.CASE_CLOSED:
            return case_closed()
        if self is WebhookEventType.USER_STATE_UPDATED:
            return user_state_updated()
        if self is WebhookEventType.ALERT_CLOSED:
            return alert_closed()
        if self is WebhookEventType.TRANSACTION_STATUS_UPDATED:
            return transaction_status_updated()
        if self is WebhookEventType.KYC_STATUS_UPDATED:
            return kyc_status_updated()
        if self is WebhookEventType.CASE_OPENED:
            return case_opened()
        if self is WebhookEventType.ALERT_OPENED:
            return alert_opened()
