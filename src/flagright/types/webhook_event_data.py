# This file was auto-generated by Fern from our API Definition.

import typing

from .alert_closed_details import AlertClosedDetails
from .case_closed_details import CaseClosedDetails
from .kyc_status_details import KycStatusDetails
from .transaction_status_details import TransactionStatusDetails
from .user_state_details import UserStateDetails

WebhookEventData = typing.Union[
    UserStateDetails, CaseClosedDetails, AlertClosedDetails, TransactionStatusDetails, KycStatusDetails
]
