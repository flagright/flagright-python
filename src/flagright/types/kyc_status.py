# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class KycStatus(str, enum.Enum):
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    EXPIRED = "EXPIRED"
    NEW = "NEW"
    CANCELLED = "CANCELLED"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    EDD_IN_PROGRESS = "EDD_IN_PROGRESS"

    def visit(
        self,
        successful: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        new: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        manual_review: typing.Callable[[], T_Result],
        edd_in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is KycStatus.SUCCESSFUL:
            return successful()
        if self is KycStatus.FAILED:
            return failed()
        if self is KycStatus.NOT_STARTED:
            return not_started()
        if self is KycStatus.IN_PROGRESS:
            return in_progress()
        if self is KycStatus.EXPIRED:
            return expired()
        if self is KycStatus.NEW:
            return new()
        if self is KycStatus.CANCELLED:
            return cancelled()
        if self is KycStatus.MANUAL_REVIEW:
            return manual_review()
        if self is KycStatus.EDD_IN_PROGRESS:
            return edd_in_progress()
