# This file was auto-generated by Fern from our API Definition.

from .ach_details import AchDetails
from .ach_payment_method import AchPaymentMethod
from .acquisition_channel import AcquisitionChannel
from .address import Address
from .alert_closed_details import AlertClosedDetails
from .alert_opened_details import AlertOpenedDetails
from .amount import Amount
from .api_error_response import ApiErrorResponse
from .batch_response import BatchResponse
from .boolean_string import BooleanString
from .business_base import BusinessBase
from .business_optional import BusinessOptional
from .business_optional_saved_payment_details_item import (
    BusinessOptionalSavedPaymentDetailsItem,
    BusinessOptionalSavedPaymentDetailsItem_Ach,
    BusinessOptionalSavedPaymentDetailsItem_Card,
    BusinessOptionalSavedPaymentDetailsItem_Cash,
    BusinessOptionalSavedPaymentDetailsItem_Check,
    BusinessOptionalSavedPaymentDetailsItem_GenericBankAccount,
    BusinessOptionalSavedPaymentDetailsItem_Iban,
    BusinessOptionalSavedPaymentDetailsItem_Mpesa,
    BusinessOptionalSavedPaymentDetailsItem_Swift,
    BusinessOptionalSavedPaymentDetailsItem_Upi,
    BusinessOptionalSavedPaymentDetailsItem_Wallet,
)
from .business_user_event_with_rules_result import BusinessUserEventWithRulesResult
from .business_user_monitoring_result import BusinessUserMonitoringResult
from .business_user_segment import BusinessUserSegment
from .business_with_rules_result import BusinessWithRulesResult
from .business_with_rules_result_saved_payment_details_item import (
    BusinessWithRulesResultSavedPaymentDetailsItem,
    BusinessWithRulesResultSavedPaymentDetailsItem_Ach,
    BusinessWithRulesResultSavedPaymentDetailsItem_Card,
    BusinessWithRulesResultSavedPaymentDetailsItem_Cash,
    BusinessWithRulesResultSavedPaymentDetailsItem_Check,
    BusinessWithRulesResultSavedPaymentDetailsItem_GenericBankAccount,
    BusinessWithRulesResultSavedPaymentDetailsItem_Iban,
    BusinessWithRulesResultSavedPaymentDetailsItem_Mpesa,
    BusinessWithRulesResultSavedPaymentDetailsItem_Swift,
    BusinessWithRulesResultSavedPaymentDetailsItem_Upi,
    BusinessWithRulesResultSavedPaymentDetailsItem_Wallet,
)
from .card_brand import CardBrand
from .card_details import CardDetails
from .card_expiry import CardExpiry
from .card_funding import CardFunding
from .card_merchant_details import CardMerchantDetails
from .card_payment_method import CardPaymentMethod
from .card_status import CardStatus
from .card_type import CardType
from .case_closed_details import CaseClosedDetails
from .case_management_event import CaseManagementEvent
from .case_management_event_case_status import CaseManagementEventCaseStatus
from .case_management_event_case_status_reason import CaseManagementEventCaseStatusReason
from .case_opened_details import CaseOpenedDetails
from .cash_payment_method import CashPaymentMethod
from .check_delivery_status import CheckDeliveryStatus
from .check_details import CheckDetails
from .check_payment_method import CheckPaymentMethod
from .company_financial_details import CompanyFinancialDetails
from .company_general_details import CompanyGeneralDetails
from .company_registration_details import CompanyRegistrationDetails
from .consumer_name import ConsumerName
from .consumer_user_event import ConsumerUserEvent
from .consumer_user_event_with_rules_result import ConsumerUserEventWithRulesResult
from .consumer_user_monitoring_result import ConsumerUserMonitoringResult
from .consumer_user_segment import ConsumerUserSegment
from .contact_details import ContactDetails
from .country_code import CountryCode
from .currency_code import CurrencyCode
from .date import Date
from .device_data import DeviceData
from .email_id import EmailId
from .employment_details import EmploymentDetails
from .employment_status import EmploymentStatus
from .executed_rule_vars import ExecutedRuleVars
from .executed_rules_result import ExecutedRulesResult
from .expected_income import ExpectedIncome
from .failed_rules_result import FailedRulesResult
from .false_positive_details import FalsePositiveDetails
from .gender import Gender
from .general_bank_account_payment_method import GeneralBankAccountPaymentMethod
from .generic_bank_account_details import GenericBankAccountDetails
from .hit_rules_details import HitRulesDetails
from .iban_details import IbanDetails
from .iban_payment_method import IbanPaymentMethod
from .kyc_status import KycStatus
from .kyc_status_details import KycStatusDetails
from .legal_document import LegalDocument
from .legal_entity import LegalEntity
from .list_data import ListData
from .list_existed import ListExisted
from .list_header import ListHeader
from .list_item import ListItem
from .list_key_metadata import ListKeyMetadata
from .list_metadata import ListMetadata
from .list_subtype import ListSubtype
from .list_type import ListType
from .martial_status import MartialStatus
from .mcc_details import MccDetails
from .mpesa_details import MpesaDetails
from .mpesa_payment_method import MpesaPaymentMethod
from .mpesa_transaction_type import MpesaTransactionType
from .origin_funds_info import OriginFundsInfo
from .payment_method import PaymentMethod
from .pep_status import PepStatus
from .person import Person
from .place_of_birth import PlaceOfBirth
from .pos_details import PosDetails
from .pos_entry_mode import PosEntryMode
from .risk_level import RiskLevel
from .rule_action import RuleAction
from .rule_failure_exception import RuleFailureException
from .rule_hit_direction import RuleHitDirection
from .rule_hit_meta import RuleHitMeta
from .rule_labels import RuleLabels
from .rule_nature import RuleNature
from .rules_results import RulesResults
from .sanctions_details import SanctionsDetails
from .sanctions_details_entity_type import SanctionsDetailsEntityType
from .sanctions_hit_context import SanctionsHitContext
from .sanctions_screening_entity import SanctionsScreeningEntity
from .source_of_funds import SourceOfFunds
from .swift_details import SwiftDetails
from .swift_payment_method import SwiftPaymentMethod
from .tag import Tag
from .transaction import Transaction
from .transaction_amount_details import TransactionAmountDetails
from .transaction_amount_limit import TransactionAmountLimit
from .transaction_base import TransactionBase
from .transaction_count_limit import TransactionCountLimit
from .transaction_destination_payment_details import (
    TransactionDestinationPaymentDetails,
    TransactionDestinationPaymentDetails_Ach,
    TransactionDestinationPaymentDetails_Card,
    TransactionDestinationPaymentDetails_Cash,
    TransactionDestinationPaymentDetails_Check,
    TransactionDestinationPaymentDetails_GenericBankAccount,
    TransactionDestinationPaymentDetails_Iban,
    TransactionDestinationPaymentDetails_Mpesa,
    TransactionDestinationPaymentDetails_Swift,
    TransactionDestinationPaymentDetails_Upi,
    TransactionDestinationPaymentDetails_Wallet,
)
from .transaction_event import TransactionEvent
from .transaction_event_monitoring_result import TransactionEventMonitoringResult
from .transaction_event_with_rules_result import TransactionEventWithRulesResult
from .transaction_limit import TransactionLimit
from .transaction_limits import TransactionLimits
from .transaction_limits_payment_method_limits import TransactionLimitsPaymentMethodLimits
from .transaction_monitoring_result import TransactionMonitoringResult
from .transaction_origin_payment_details import (
    TransactionOriginPaymentDetails,
    TransactionOriginPaymentDetails_Ach,
    TransactionOriginPaymentDetails_Card,
    TransactionOriginPaymentDetails_Cash,
    TransactionOriginPaymentDetails_Check,
    TransactionOriginPaymentDetails_GenericBankAccount,
    TransactionOriginPaymentDetails_Iban,
    TransactionOriginPaymentDetails_Mpesa,
    TransactionOriginPaymentDetails_Swift,
    TransactionOriginPaymentDetails_Upi,
    TransactionOriginPaymentDetails_Wallet,
)
from .transaction_risk_scoring_result import TransactionRiskScoringResult
from .transaction_state import TransactionState
from .transaction_status_details import TransactionStatusDetails
from .transaction_type import TransactionType
from .transaction_updatable import TransactionUpdatable
from .transaction_updatable_destination_payment_details import (
    TransactionUpdatableDestinationPaymentDetails,
    TransactionUpdatableDestinationPaymentDetails_Ach,
    TransactionUpdatableDestinationPaymentDetails_Card,
    TransactionUpdatableDestinationPaymentDetails_Cash,
    TransactionUpdatableDestinationPaymentDetails_Check,
    TransactionUpdatableDestinationPaymentDetails_GenericBankAccount,
    TransactionUpdatableDestinationPaymentDetails_Iban,
    TransactionUpdatableDestinationPaymentDetails_Mpesa,
    TransactionUpdatableDestinationPaymentDetails_Swift,
    TransactionUpdatableDestinationPaymentDetails_Upi,
    TransactionUpdatableDestinationPaymentDetails_Wallet,
)
from .transaction_updatable_origin_payment_details import (
    TransactionUpdatableOriginPaymentDetails,
    TransactionUpdatableOriginPaymentDetails_Ach,
    TransactionUpdatableOriginPaymentDetails_Card,
    TransactionUpdatableOriginPaymentDetails_Cash,
    TransactionUpdatableOriginPaymentDetails_Check,
    TransactionUpdatableOriginPaymentDetails_GenericBankAccount,
    TransactionUpdatableOriginPaymentDetails_Iban,
    TransactionUpdatableOriginPaymentDetails_Mpesa,
    TransactionUpdatableOriginPaymentDetails_Swift,
    TransactionUpdatableOriginPaymentDetails_Upi,
    TransactionUpdatableOriginPaymentDetails_Wallet,
)
from .transaction_with_rules_result import TransactionWithRulesResult
from .transaction_with_rules_result_destination_payment_details import (
    TransactionWithRulesResultDestinationPaymentDetails,
    TransactionWithRulesResultDestinationPaymentDetails_Ach,
    TransactionWithRulesResultDestinationPaymentDetails_Card,
    TransactionWithRulesResultDestinationPaymentDetails_Cash,
    TransactionWithRulesResultDestinationPaymentDetails_Check,
    TransactionWithRulesResultDestinationPaymentDetails_GenericBankAccount,
    TransactionWithRulesResultDestinationPaymentDetails_Iban,
    TransactionWithRulesResultDestinationPaymentDetails_Mpesa,
    TransactionWithRulesResultDestinationPaymentDetails_Swift,
    TransactionWithRulesResultDestinationPaymentDetails_Upi,
    TransactionWithRulesResultDestinationPaymentDetails_Wallet,
)
from .transaction_with_rules_result_origin_payment_details import (
    TransactionWithRulesResultOriginPaymentDetails,
    TransactionWithRulesResultOriginPaymentDetails_Ach,
    TransactionWithRulesResultOriginPaymentDetails_Card,
    TransactionWithRulesResultOriginPaymentDetails_Cash,
    TransactionWithRulesResultOriginPaymentDetails_Check,
    TransactionWithRulesResultOriginPaymentDetails_GenericBankAccount,
    TransactionWithRulesResultOriginPaymentDetails_Iban,
    TransactionWithRulesResultOriginPaymentDetails_Mpesa,
    TransactionWithRulesResultOriginPaymentDetails_Swift,
    TransactionWithRulesResultOriginPaymentDetails_Upi,
    TransactionWithRulesResultOriginPaymentDetails_Wallet,
)
from .upi_details import UpiDetails
from .upi_payment_method import UpiPaymentMethod
from .user import User
from .user_base import UserBase
from .user_details import UserDetails
from .user_entity_link import UserEntityLink
from .user_optional import UserOptional
from .user_optional_saved_payment_details_item import (
    UserOptionalSavedPaymentDetailsItem,
    UserOptionalSavedPaymentDetailsItem_Ach,
    UserOptionalSavedPaymentDetailsItem_Card,
    UserOptionalSavedPaymentDetailsItem_Cash,
    UserOptionalSavedPaymentDetailsItem_Check,
    UserOptionalSavedPaymentDetailsItem_GenericBankAccount,
    UserOptionalSavedPaymentDetailsItem_Iban,
    UserOptionalSavedPaymentDetailsItem_Mpesa,
    UserOptionalSavedPaymentDetailsItem_Swift,
    UserOptionalSavedPaymentDetailsItem_Upi,
    UserOptionalSavedPaymentDetailsItem_Wallet,
)
from .user_registration_status import UserRegistrationStatus
from .user_risk_score_details import UserRiskScoreDetails
from .user_rules_result import UserRulesResult
from .user_saved_payment_details_item import (
    UserSavedPaymentDetailsItem,
    UserSavedPaymentDetailsItem_Ach,
    UserSavedPaymentDetailsItem_Card,
    UserSavedPaymentDetailsItem_Cash,
    UserSavedPaymentDetailsItem_Check,
    UserSavedPaymentDetailsItem_GenericBankAccount,
    UserSavedPaymentDetailsItem_Iban,
    UserSavedPaymentDetailsItem_Mpesa,
    UserSavedPaymentDetailsItem_Swift,
    UserSavedPaymentDetailsItem_Upi,
    UserSavedPaymentDetailsItem_Wallet,
)
from .user_state import UserState
from .user_state_details import UserStateDetails
from .user_with_rules_result import UserWithRulesResult
from .user_with_rules_result_saved_payment_details_item import (
    UserWithRulesResultSavedPaymentDetailsItem,
    UserWithRulesResultSavedPaymentDetailsItem_Ach,
    UserWithRulesResultSavedPaymentDetailsItem_Card,
    UserWithRulesResultSavedPaymentDetailsItem_Cash,
    UserWithRulesResultSavedPaymentDetailsItem_Check,
    UserWithRulesResultSavedPaymentDetailsItem_GenericBankAccount,
    UserWithRulesResultSavedPaymentDetailsItem_Iban,
    UserWithRulesResultSavedPaymentDetailsItem_Mpesa,
    UserWithRulesResultSavedPaymentDetailsItem_Swift,
    UserWithRulesResultSavedPaymentDetailsItem_Upi,
    UserWithRulesResultSavedPaymentDetailsItem_Wallet,
)
from .wallet_details import WalletDetails
from .wallet_network import WalletNetwork
from .wallet_payment_method import WalletPaymentMethod
from .webhook_event import WebhookEvent
from .webhook_event_base import WebhookEventBase
from .webhook_event_base_triggered_by import WebhookEventBaseTriggeredBy
from .webhook_event_data import WebhookEventData
from .webhook_event_triggered_by import WebhookEventTriggeredBy
from .webhook_event_type import WebhookEventType

__all__ = [
    "AchDetails",
    "AchPaymentMethod",
    "AcquisitionChannel",
    "Address",
    "AlertClosedDetails",
    "AlertOpenedDetails",
    "Amount",
    "ApiErrorResponse",
    "BatchResponse",
    "BooleanString",
    "BusinessBase",
    "BusinessOptional",
    "BusinessOptionalSavedPaymentDetailsItem",
    "BusinessOptionalSavedPaymentDetailsItem_Ach",
    "BusinessOptionalSavedPaymentDetailsItem_Card",
    "BusinessOptionalSavedPaymentDetailsItem_Cash",
    "BusinessOptionalSavedPaymentDetailsItem_Check",
    "BusinessOptionalSavedPaymentDetailsItem_GenericBankAccount",
    "BusinessOptionalSavedPaymentDetailsItem_Iban",
    "BusinessOptionalSavedPaymentDetailsItem_Mpesa",
    "BusinessOptionalSavedPaymentDetailsItem_Swift",
    "BusinessOptionalSavedPaymentDetailsItem_Upi",
    "BusinessOptionalSavedPaymentDetailsItem_Wallet",
    "BusinessUserEventWithRulesResult",
    "BusinessUserMonitoringResult",
    "BusinessUserSegment",
    "BusinessWithRulesResult",
    "BusinessWithRulesResultSavedPaymentDetailsItem",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Ach",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Card",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Cash",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Check",
    "BusinessWithRulesResultSavedPaymentDetailsItem_GenericBankAccount",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Iban",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Mpesa",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Swift",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Upi",
    "BusinessWithRulesResultSavedPaymentDetailsItem_Wallet",
    "CardBrand",
    "CardDetails",
    "CardExpiry",
    "CardFunding",
    "CardMerchantDetails",
    "CardPaymentMethod",
    "CardStatus",
    "CardType",
    "CaseClosedDetails",
    "CaseManagementEvent",
    "CaseManagementEventCaseStatus",
    "CaseManagementEventCaseStatusReason",
    "CaseOpenedDetails",
    "CashPaymentMethod",
    "CheckDeliveryStatus",
    "CheckDetails",
    "CheckPaymentMethod",
    "CompanyFinancialDetails",
    "CompanyGeneralDetails",
    "CompanyRegistrationDetails",
    "ConsumerName",
    "ConsumerUserEvent",
    "ConsumerUserEventWithRulesResult",
    "ConsumerUserMonitoringResult",
    "ConsumerUserSegment",
    "ContactDetails",
    "CountryCode",
    "CurrencyCode",
    "Date",
    "DeviceData",
    "EmailId",
    "EmploymentDetails",
    "EmploymentStatus",
    "ExecutedRuleVars",
    "ExecutedRulesResult",
    "ExpectedIncome",
    "FailedRulesResult",
    "FalsePositiveDetails",
    "Gender",
    "GeneralBankAccountPaymentMethod",
    "GenericBankAccountDetails",
    "HitRulesDetails",
    "IbanDetails",
    "IbanPaymentMethod",
    "KycStatus",
    "KycStatusDetails",
    "LegalDocument",
    "LegalEntity",
    "ListData",
    "ListExisted",
    "ListHeader",
    "ListItem",
    "ListKeyMetadata",
    "ListMetadata",
    "ListSubtype",
    "ListType",
    "MartialStatus",
    "MccDetails",
    "MpesaDetails",
    "MpesaPaymentMethod",
    "MpesaTransactionType",
    "OriginFundsInfo",
    "PaymentMethod",
    "PepStatus",
    "Person",
    "PlaceOfBirth",
    "PosDetails",
    "PosEntryMode",
    "RiskLevel",
    "RuleAction",
    "RuleFailureException",
    "RuleHitDirection",
    "RuleHitMeta",
    "RuleLabels",
    "RuleNature",
    "RulesResults",
    "SanctionsDetails",
    "SanctionsDetailsEntityType",
    "SanctionsHitContext",
    "SanctionsScreeningEntity",
    "SourceOfFunds",
    "SwiftDetails",
    "SwiftPaymentMethod",
    "Tag",
    "Transaction",
    "TransactionAmountDetails",
    "TransactionAmountLimit",
    "TransactionBase",
    "TransactionCountLimit",
    "TransactionDestinationPaymentDetails",
    "TransactionDestinationPaymentDetails_Ach",
    "TransactionDestinationPaymentDetails_Card",
    "TransactionDestinationPaymentDetails_Cash",
    "TransactionDestinationPaymentDetails_Check",
    "TransactionDestinationPaymentDetails_GenericBankAccount",
    "TransactionDestinationPaymentDetails_Iban",
    "TransactionDestinationPaymentDetails_Mpesa",
    "TransactionDestinationPaymentDetails_Swift",
    "TransactionDestinationPaymentDetails_Upi",
    "TransactionDestinationPaymentDetails_Wallet",
    "TransactionEvent",
    "TransactionEventMonitoringResult",
    "TransactionEventWithRulesResult",
    "TransactionLimit",
    "TransactionLimits",
    "TransactionLimitsPaymentMethodLimits",
    "TransactionMonitoringResult",
    "TransactionOriginPaymentDetails",
    "TransactionOriginPaymentDetails_Ach",
    "TransactionOriginPaymentDetails_Card",
    "TransactionOriginPaymentDetails_Cash",
    "TransactionOriginPaymentDetails_Check",
    "TransactionOriginPaymentDetails_GenericBankAccount",
    "TransactionOriginPaymentDetails_Iban",
    "TransactionOriginPaymentDetails_Mpesa",
    "TransactionOriginPaymentDetails_Swift",
    "TransactionOriginPaymentDetails_Upi",
    "TransactionOriginPaymentDetails_Wallet",
    "TransactionRiskScoringResult",
    "TransactionState",
    "TransactionStatusDetails",
    "TransactionType",
    "TransactionUpdatable",
    "TransactionUpdatableDestinationPaymentDetails",
    "TransactionUpdatableDestinationPaymentDetails_Ach",
    "TransactionUpdatableDestinationPaymentDetails_Card",
    "TransactionUpdatableDestinationPaymentDetails_Cash",
    "TransactionUpdatableDestinationPaymentDetails_Check",
    "TransactionUpdatableDestinationPaymentDetails_GenericBankAccount",
    "TransactionUpdatableDestinationPaymentDetails_Iban",
    "TransactionUpdatableDestinationPaymentDetails_Mpesa",
    "TransactionUpdatableDestinationPaymentDetails_Swift",
    "TransactionUpdatableDestinationPaymentDetails_Upi",
    "TransactionUpdatableDestinationPaymentDetails_Wallet",
    "TransactionUpdatableOriginPaymentDetails",
    "TransactionUpdatableOriginPaymentDetails_Ach",
    "TransactionUpdatableOriginPaymentDetails_Card",
    "TransactionUpdatableOriginPaymentDetails_Cash",
    "TransactionUpdatableOriginPaymentDetails_Check",
    "TransactionUpdatableOriginPaymentDetails_GenericBankAccount",
    "TransactionUpdatableOriginPaymentDetails_Iban",
    "TransactionUpdatableOriginPaymentDetails_Mpesa",
    "TransactionUpdatableOriginPaymentDetails_Swift",
    "TransactionUpdatableOriginPaymentDetails_Upi",
    "TransactionUpdatableOriginPaymentDetails_Wallet",
    "TransactionWithRulesResult",
    "TransactionWithRulesResultDestinationPaymentDetails",
    "TransactionWithRulesResultDestinationPaymentDetails_Ach",
    "TransactionWithRulesResultDestinationPaymentDetails_Card",
    "TransactionWithRulesResultDestinationPaymentDetails_Cash",
    "TransactionWithRulesResultDestinationPaymentDetails_Check",
    "TransactionWithRulesResultDestinationPaymentDetails_GenericBankAccount",
    "TransactionWithRulesResultDestinationPaymentDetails_Iban",
    "TransactionWithRulesResultDestinationPaymentDetails_Mpesa",
    "TransactionWithRulesResultDestinationPaymentDetails_Swift",
    "TransactionWithRulesResultDestinationPaymentDetails_Upi",
    "TransactionWithRulesResultDestinationPaymentDetails_Wallet",
    "TransactionWithRulesResultOriginPaymentDetails",
    "TransactionWithRulesResultOriginPaymentDetails_Ach",
    "TransactionWithRulesResultOriginPaymentDetails_Card",
    "TransactionWithRulesResultOriginPaymentDetails_Cash",
    "TransactionWithRulesResultOriginPaymentDetails_Check",
    "TransactionWithRulesResultOriginPaymentDetails_GenericBankAccount",
    "TransactionWithRulesResultOriginPaymentDetails_Iban",
    "TransactionWithRulesResultOriginPaymentDetails_Mpesa",
    "TransactionWithRulesResultOriginPaymentDetails_Swift",
    "TransactionWithRulesResultOriginPaymentDetails_Upi",
    "TransactionWithRulesResultOriginPaymentDetails_Wallet",
    "UpiDetails",
    "UpiPaymentMethod",
    "User",
    "UserBase",
    "UserDetails",
    "UserEntityLink",
    "UserOptional",
    "UserOptionalSavedPaymentDetailsItem",
    "UserOptionalSavedPaymentDetailsItem_Ach",
    "UserOptionalSavedPaymentDetailsItem_Card",
    "UserOptionalSavedPaymentDetailsItem_Cash",
    "UserOptionalSavedPaymentDetailsItem_Check",
    "UserOptionalSavedPaymentDetailsItem_GenericBankAccount",
    "UserOptionalSavedPaymentDetailsItem_Iban",
    "UserOptionalSavedPaymentDetailsItem_Mpesa",
    "UserOptionalSavedPaymentDetailsItem_Swift",
    "UserOptionalSavedPaymentDetailsItem_Upi",
    "UserOptionalSavedPaymentDetailsItem_Wallet",
    "UserRegistrationStatus",
    "UserRiskScoreDetails",
    "UserRulesResult",
    "UserSavedPaymentDetailsItem",
    "UserSavedPaymentDetailsItem_Ach",
    "UserSavedPaymentDetailsItem_Card",
    "UserSavedPaymentDetailsItem_Cash",
    "UserSavedPaymentDetailsItem_Check",
    "UserSavedPaymentDetailsItem_GenericBankAccount",
    "UserSavedPaymentDetailsItem_Iban",
    "UserSavedPaymentDetailsItem_Mpesa",
    "UserSavedPaymentDetailsItem_Swift",
    "UserSavedPaymentDetailsItem_Upi",
    "UserSavedPaymentDetailsItem_Wallet",
    "UserState",
    "UserStateDetails",
    "UserWithRulesResult",
    "UserWithRulesResultSavedPaymentDetailsItem",
    "UserWithRulesResultSavedPaymentDetailsItem_Ach",
    "UserWithRulesResultSavedPaymentDetailsItem_Card",
    "UserWithRulesResultSavedPaymentDetailsItem_Cash",
    "UserWithRulesResultSavedPaymentDetailsItem_Check",
    "UserWithRulesResultSavedPaymentDetailsItem_GenericBankAccount",
    "UserWithRulesResultSavedPaymentDetailsItem_Iban",
    "UserWithRulesResultSavedPaymentDetailsItem_Mpesa",
    "UserWithRulesResultSavedPaymentDetailsItem_Swift",
    "UserWithRulesResultSavedPaymentDetailsItem_Upi",
    "UserWithRulesResultSavedPaymentDetailsItem_Wallet",
    "WalletDetails",
    "WalletNetwork",
    "WalletPaymentMethod",
    "WebhookEvent",
    "WebhookEventBase",
    "WebhookEventBaseTriggeredBy",
    "WebhookEventData",
    "WebhookEventTriggeredBy",
    "WebhookEventType",
]
