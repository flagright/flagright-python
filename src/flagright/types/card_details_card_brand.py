# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CardDetailsCardBrand(str, enum.Enum):
    """
    Brand of Card
    """

    VISA = "VISA"
    MASTERCARD = "MASTERCARD"
    AMERICAN_EXPRESS = "AMERICAN_EXPRESS"
    DISCOVER = "DISCOVER"
    UNIONPAY = "UNIONPAY"
    RUPAY = "RUPAY"
    JCB = "JCB"

    def visit(
        self,
        visa: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        american_express: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        unionpay: typing.Callable[[], T_Result],
        rupay: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardDetailsCardBrand.VISA:
            return visa()
        if self is CardDetailsCardBrand.MASTERCARD:
            return mastercard()
        if self is CardDetailsCardBrand.AMERICAN_EXPRESS:
            return american_express()
        if self is CardDetailsCardBrand.DISCOVER:
            return discover()
        if self is CardDetailsCardBrand.UNIONPAY:
            return unionpay()
        if self is CardDetailsCardBrand.RUPAY:
            return rupay()
        if self is CardDetailsCardBrand.JCB:
            return jcb()
