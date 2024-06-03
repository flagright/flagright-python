# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from ....types.ach_details import AchDetails
from ....types.card_details import CardDetails
from ....types.check_details import CheckDetails
from ....types.generic_bank_account_details import GenericBankAccountDetails
from ....types.iban_details import IbanDetails
from ....types.mpesa_details import MpesaDetails
from ....types.swift_details import SwiftDetails
from ....types.upi_details import UpiDetails
from ....types.wallet_details import WalletDetails


class BusinessSavedPaymentDetailsItem_Card(CardDetails):
    method: typing_extensions.Literal["CARD"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_GenericBankAccount(GenericBankAccountDetails):
    method: typing_extensions.Literal["GENERIC_BANK_ACCOUNT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Iban(IbanDetails):
    method: typing_extensions.Literal["IBAN"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Ach(AchDetails):
    method: typing_extensions.Literal["ACH"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Swift(SwiftDetails):
    method: typing_extensions.Literal["SWIFT"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Mpesa(MpesaDetails):
    method: typing_extensions.Literal["MPESA"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Upi(UpiDetails):
    method: typing_extensions.Literal["UPI"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Wallet(WalletDetails):
    method: typing_extensions.Literal["WALLET"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class BusinessSavedPaymentDetailsItem_Check(CheckDetails):
    method: typing_extensions.Literal["CHECK"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


BusinessSavedPaymentDetailsItem = typing.Union[
    BusinessSavedPaymentDetailsItem_Card,
    BusinessSavedPaymentDetailsItem_GenericBankAccount,
    BusinessSavedPaymentDetailsItem_Iban,
    BusinessSavedPaymentDetailsItem_Ach,
    BusinessSavedPaymentDetailsItem_Swift,
    BusinessSavedPaymentDetailsItem_Mpesa,
    BusinessSavedPaymentDetailsItem_Upi,
    BusinessSavedPaymentDetailsItem_Wallet,
    BusinessSavedPaymentDetailsItem_Check,
]