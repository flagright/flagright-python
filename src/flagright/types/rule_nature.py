# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RuleNature(str, enum.Enum):
    AML = "AML"
    FRAUD = "FRAUD"
    CTF = "CTF"
    SCREENING = "SCREENING"

    def visit(
        self,
        aml: typing.Callable[[], T_Result],
        fraud: typing.Callable[[], T_Result],
        ctf: typing.Callable[[], T_Result],
        screening: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RuleNature.AML:
            return aml()
        if self is RuleNature.FRAUD:
            return fraud()
        if self is RuleNature.CTF:
            return ctf()
        if self is RuleNature.SCREENING:
            return screening()
