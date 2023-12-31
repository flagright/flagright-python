# This file was auto-generated by Fern from our API Definition.

import typing

from .ach_details import AchDetails
from .card_details import CardDetails
from .check_details import CheckDetails
from .generic_bank_account_details import GenericBankAccountDetails
from .iban_details import IbanDetails
from .mpesa_details import MpesaDetails
from .swift_details import SwiftDetails
from .upi_details import UpiDetails
from .wallet_details import WalletDetails

BusinessOptionalSavedPaymentDetailsItem = typing.Union[
    CardDetails,
    GenericBankAccountDetails,
    IbanDetails,
    AchDetails,
    SwiftDetails,
    MpesaDetails,
    UpiDetails,
    WalletDetails,
    CheckDetails,
]
