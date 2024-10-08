# This file was auto-generated by Fern from our API Definition.

import typing

from .alert_closed_details import AlertClosedDetails
from .alert_opened_details import AlertOpenedDetails
from .case_closed_details import CaseClosedDetails
from .case_opened_details import CaseOpenedDetails
from .cra_risk_level_updated_details import CraRiskLevelUpdatedDetails
from .kyc_status_details import KycStatusDetails
from .transaction_status_details import TransactionStatusDetails
from .user_state_details import UserStateDetails
from .user_tags_update import UserTagsUpdate

WebhookEventData = typing.Union[
    UserStateDetails,
    CaseClosedDetails,
    CaseOpenedDetails,
    AlertClosedDetails,
    AlertOpenedDetails,
    TransactionStatusDetails,
    KycStatusDetails,
    UserTagsUpdate,
    CraRiskLevelUpdatedDetails,
]
