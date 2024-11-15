# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListSubtype(str, enum.Enum):
    USER_ID = "USER_ID"
    CARD_FINGERPRINT_NUMBER = "CARD_FINGERPRINT_NUMBER"
    IBAN_NUMBER = "IBAN_NUMBER"
    BANK_ACCOUNT_NUMBER = "BANK_ACCOUNT_NUMBER"
    ACH_ACCOUNT_NUMBER = "ACH_ACCOUNT_NUMBER"
    SWIFT_ACCOUNT_NUMBER = "SWIFT_ACCOUNT_NUMBER"
    BIC = "BIC"
    BANK_SWIFT_CODE = "BANK_SWIFT_CODE"
    UPI_IDENTIFYING_NUMBER = "UPI_IDENTIFYING_NUMBER"
    IP_ADDRESS = "IP_ADDRESS"
    DEVICE_IDENTIFIER = "DEVICE_IDENTIFIER"
    STRING = "STRING"
    COUNTRY = "COUNTRY"

    def visit(
        self,
        user_id: typing.Callable[[], T_Result],
        card_fingerprint_number: typing.Callable[[], T_Result],
        iban_number: typing.Callable[[], T_Result],
        bank_account_number: typing.Callable[[], T_Result],
        ach_account_number: typing.Callable[[], T_Result],
        swift_account_number: typing.Callable[[], T_Result],
        bic: typing.Callable[[], T_Result],
        bank_swift_code: typing.Callable[[], T_Result],
        upi_identifying_number: typing.Callable[[], T_Result],
        ip_address: typing.Callable[[], T_Result],
        device_identifier: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListSubtype.USER_ID:
            return user_id()
        if self is ListSubtype.CARD_FINGERPRINT_NUMBER:
            return card_fingerprint_number()
        if self is ListSubtype.IBAN_NUMBER:
            return iban_number()
        if self is ListSubtype.BANK_ACCOUNT_NUMBER:
            return bank_account_number()
        if self is ListSubtype.ACH_ACCOUNT_NUMBER:
            return ach_account_number()
        if self is ListSubtype.SWIFT_ACCOUNT_NUMBER:
            return swift_account_number()
        if self is ListSubtype.BIC:
            return bic()
        if self is ListSubtype.BANK_SWIFT_CODE:
            return bank_swift_code()
        if self is ListSubtype.UPI_IDENTIFYING_NUMBER:
            return upi_identifying_number()
        if self is ListSubtype.IP_ADDRESS:
            return ip_address()
        if self is ListSubtype.DEVICE_IDENTIFIER:
            return device_identifier()
        if self is ListSubtype.STRING:
            return string()
        if self is ListSubtype.COUNTRY:
            return country()
