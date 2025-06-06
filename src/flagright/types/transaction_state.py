# This file was auto-generated by Fern from our API Definition.

import typing

TransactionState = typing.Union[
    typing.Literal[
        "CREATED", "PROCESSING", "SENT", "EXPIRED", "DECLINED", "SUSPENDED", "REFUNDED", "SUCCESSFUL", "REVERSED"
    ],
    typing.Any,
]
