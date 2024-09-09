# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .ach_details import AchDetails
from .card_details import CardDetails
from .check_details import CheckDetails
from .generic_bank_account_details import GenericBankAccountDetails
from .iban_details import IbanDetails
from .mpesa_details import MpesaDetails
from .swift_details import SwiftDetails
from .upi_details import UpiDetails
from .wallet_details import WalletDetails


class TransactionWithRulesResultOriginPaymentDetails_Card(CardDetails):
    method: typing_extensions.Literal["CARD"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_GenericBankAccount(GenericBankAccountDetails):
    method: typing_extensions.Literal["GENERIC_BANK_ACCOUNT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Iban(IbanDetails):
    method: typing_extensions.Literal["IBAN"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Ach(AchDetails):
    method: typing_extensions.Literal["ACH"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Swift(SwiftDetails):
    method: typing_extensions.Literal["SWIFT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Mpesa(MpesaDetails):
    method: typing_extensions.Literal["MPESA"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Upi(UpiDetails):
    method: typing_extensions.Literal["UPI"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Wallet(WalletDetails):
    method: typing_extensions.Literal["WALLET"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Check(CheckDetails):
    method: typing_extensions.Literal["CHECK"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class TransactionWithRulesResultOriginPaymentDetails_Cash(CheckDetails):
    method: typing_extensions.Literal["CASH"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


TransactionWithRulesResultOriginPaymentDetails = typing.Union[
    TransactionWithRulesResultOriginPaymentDetails_Card,
    TransactionWithRulesResultOriginPaymentDetails_GenericBankAccount,
    TransactionWithRulesResultOriginPaymentDetails_Iban,
    TransactionWithRulesResultOriginPaymentDetails_Ach,
    TransactionWithRulesResultOriginPaymentDetails_Swift,
    TransactionWithRulesResultOriginPaymentDetails_Mpesa,
    TransactionWithRulesResultOriginPaymentDetails_Upi,
    TransactionWithRulesResultOriginPaymentDetails_Wallet,
    TransactionWithRulesResultOriginPaymentDetails_Check,
    TransactionWithRulesResultOriginPaymentDetails_Cash,
]
