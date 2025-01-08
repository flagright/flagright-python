# This file was auto-generated by Fern from our API Definition.

from .types import (
    AchDetails,
    AchPaymentMethod,
    AcquisitionChannel,
    Address,
    AlertClosedDetails,
    AlertOpenedDetails,
    Amount,
    ApiErrorResponse,
    BatchResponse,
    BatchResponseFailedRecord,
    BatchResponseStatus,
    BooleanString,
    Business,
    BusinessBase,
    BusinessOptional,
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
    BusinessSavedPaymentDetailsItem,
    BusinessSavedPaymentDetailsItem_Ach,
    BusinessSavedPaymentDetailsItem_Card,
    BusinessSavedPaymentDetailsItem_Cash,
    BusinessSavedPaymentDetailsItem_Check,
    BusinessSavedPaymentDetailsItem_GenericBankAccount,
    BusinessSavedPaymentDetailsItem_Iban,
    BusinessSavedPaymentDetailsItem_Mpesa,
    BusinessSavedPaymentDetailsItem_Swift,
    BusinessSavedPaymentDetailsItem_Upi,
    BusinessSavedPaymentDetailsItem_Wallet,
    BusinessUserEvent,
    BusinessUserEventWithRulesResult,
    BusinessUserMonitoringResult,
    BusinessUserSegment,
    BusinessWithRulesResult,
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
    CardBrand,
    CardDetails,
    CardExpiry,
    CardFunding,
    CardMerchantDetails,
    CardPaymentMethod,
    CardStatus,
    CardType,
    CaseClosedDetails,
    CaseManagementEvent,
    CaseManagementEventCaseStatus,
    CaseManagementEventCaseStatusReason,
    CaseOpenedDetails,
    CashDetails,
    CashPaymentMethod,
    CheckDeliveryStatus,
    CheckDetails,
    CheckPaymentMethod,
    CompanyFinancialDetails,
    CompanyGeneralDetails,
    CompanyRegistrationDetails,
    ConsumerName,
    ConsumerUserEvent,
    ConsumerUserEventWithRulesResult,
    ConsumerUserMonitoringResult,
    ConsumerUserSegment,
    ContactDetails,
    CountryCode,
    CraRiskLevelUpdatedDetails,
    CurrencyCode,
    Date,
    DeviceData,
    EmailId,
    EmploymentDetails,
    EmploymentStatus,
    ExecutedLogicVars,
    ExecutedRulesResult,
    ExpectedIncome,
    FailedRulesResult,
    FalsePositiveDetails,
    FileInfo,
    Gender,
    GeneralBankAccountPaymentMethod,
    GenericBankAccountDetails,
    HitRulesDetails,
    IbanDetails,
    IbanPaymentMethod,
    KycStatus,
    KycStatusDetails,
    LegalDocument,
    LegalEntity,
    ListData,
    ListExisted,
    ListHeader,
    ListItem,
    ListKeyMetadata,
    ListMetadata,
    ListSubtype,
    ListType,
    ListUpdatedDetails,
    ListUpdatedDetailsAction,
    MaritalStatus,
    MccDetails,
    MpesaDetails,
    MpesaPaymentMethod,
    MpesaTransactionType,
    OriginFundsInfo,
    PaymentMethod,
    PepRank,
    PepStatus,
    Person,
    PersonAttachment,
    PlaceOfBirth,
    PosDetails,
    PosEntryMode,
    RiskLevel,
    RuleAction,
    RuleFailureException,
    RuleHitDirection,
    RuleHitMeta,
    RuleLabels,
    RuleNature,
    RulesResults,
    SanctionsDetails,
    SanctionsDetailsEntityType,
    SanctionsHitContext,
    SanctionsScreeningEntity,
    SourceOfFunds,
    SwiftDetails,
    SwiftPaymentMethod,
    Tag,
    Transaction,
    TransactionAmountDetails,
    TransactionAmountLimit,
    TransactionBase,
    TransactionCountLimit,
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
    TransactionEvent,
    TransactionEventMonitoringResult,
    TransactionEventWithRulesResult,
    TransactionLimit,
    TransactionLimits,
    TransactionLimitsPaymentMethodLimits,
    TransactionMonitoringResult,
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
    TransactionRiskScoringResult,
    TransactionState,
    TransactionStatusDetails,
    TransactionType,
    TransactionUpdatable,
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
    TransactionWithRulesResult,
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
    UpiDetails,
    UpiPaymentMethod,
    User,
    UserBase,
    UserDetails,
    UserEntityLink,
    UserOptional,
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
    UserRegistrationStatus,
    UserRiskScoreDetails,
    UserRulesResult,
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
    UserState,
    UserStateDetails,
    UserTag,
    UserTagsUpdate,
    UserWithRulesResult,
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
    WalletDetails,
    WalletNetwork,
    WalletPaymentMethod,
    WebhookEvent,
    WebhookEventBase,
    WebhookEventBaseTriggeredBy,
    WebhookEventData,
    WebhookEventTriggeredBy,
    WebhookEventType,
)
from .errors import BadRequestError, ConflictError, TooManyRequestsError, UnauthorizedError
from .resources import (
    BusinessUsersCreateResponse,
    ConsumerUsersCreateResponse,
    TransactionsVerifyResponse,
    batch,
    business_user_events,
    business_users,
    consumer_user_events,
    consumer_users,
    transaction_events,
    transactions,
)
from .environment import FlagrightEnvironment

__all__ = [
    "AchDetails",
    "AchPaymentMethod",
    "AcquisitionChannel",
    "Address",
    "AlertClosedDetails",
    "AlertOpenedDetails",
    "Amount",
    "ApiErrorResponse",
    "BadRequestError",
    "BatchResponse",
    "BatchResponseFailedRecord",
    "BatchResponseStatus",
    "BooleanString",
    "Business",
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
    "BusinessSavedPaymentDetailsItem",
    "BusinessSavedPaymentDetailsItem_Ach",
    "BusinessSavedPaymentDetailsItem_Card",
    "BusinessSavedPaymentDetailsItem_Cash",
    "BusinessSavedPaymentDetailsItem_Check",
    "BusinessSavedPaymentDetailsItem_GenericBankAccount",
    "BusinessSavedPaymentDetailsItem_Iban",
    "BusinessSavedPaymentDetailsItem_Mpesa",
    "BusinessSavedPaymentDetailsItem_Swift",
    "BusinessSavedPaymentDetailsItem_Upi",
    "BusinessSavedPaymentDetailsItem_Wallet",
    "BusinessUserEvent",
    "BusinessUserEventWithRulesResult",
    "BusinessUserMonitoringResult",
    "BusinessUserSegment",
    "BusinessUsersCreateResponse",
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
    "CashDetails",
    "CashPaymentMethod",
    "CheckDeliveryStatus",
    "CheckDetails",
    "CheckPaymentMethod",
    "CompanyFinancialDetails",
    "CompanyGeneralDetails",
    "CompanyRegistrationDetails",
    "ConflictError",
    "ConsumerName",
    "ConsumerUserEvent",
    "ConsumerUserEventWithRulesResult",
    "ConsumerUserMonitoringResult",
    "ConsumerUserSegment",
    "ConsumerUsersCreateResponse",
    "ContactDetails",
    "CountryCode",
    "CraRiskLevelUpdatedDetails",
    "CurrencyCode",
    "Date",
    "DeviceData",
    "EmailId",
    "EmploymentDetails",
    "EmploymentStatus",
    "ExecutedLogicVars",
    "ExecutedRulesResult",
    "ExpectedIncome",
    "FailedRulesResult",
    "FalsePositiveDetails",
    "FileInfo",
    "FlagrightEnvironment",
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
    "ListUpdatedDetails",
    "ListUpdatedDetailsAction",
    "MaritalStatus",
    "MccDetails",
    "MpesaDetails",
    "MpesaPaymentMethod",
    "MpesaTransactionType",
    "OriginFundsInfo",
    "PaymentMethod",
    "PepRank",
    "PepStatus",
    "Person",
    "PersonAttachment",
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
    "TooManyRequestsError",
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
    "TransactionsVerifyResponse",
    "UnauthorizedError",
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
    "UserTag",
    "UserTagsUpdate",
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
    "batch",
    "business_user_events",
    "business_users",
    "consumer_user_events",
    "consumer_users",
    "transaction_events",
    "transactions",
]
