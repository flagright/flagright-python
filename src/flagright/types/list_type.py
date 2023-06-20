# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListType(str, enum.Enum):
    WHITELIST = "WHITELIST"
    BLACKLIST = "BLACKLIST"
    FLAGRIGHT_LIBRARY = "FLAGRIGHT_LIBRARY"

    def visit(
        self,
        whitelist: typing.Callable[[], T_Result],
        blacklist: typing.Callable[[], T_Result],
        flagright_library: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListType.WHITELIST:
            return whitelist()
        if self is ListType.BLACKLIST:
            return blacklist()
        if self is ListType.FLAGRIGHT_LIBRARY:
            return flagright_library()
