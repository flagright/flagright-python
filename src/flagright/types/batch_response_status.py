# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BatchResponseStatus(str, enum.Enum):
    """
    Status of the batch response
    """

    SUCCESS = "SUCCESS"
    PARTIAL_FAILURE = "PARTIAL_FAILURE"
    FAILURE = "FAILURE"

    def visit(
        self,
        success: typing.Callable[[], T_Result],
        partial_failure: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BatchResponseStatus.SUCCESS:
            return success()
        if self is BatchResponseStatus.PARTIAL_FAILURE:
            return partial_failure()
        if self is BatchResponseStatus.FAILURE:
            return failure()