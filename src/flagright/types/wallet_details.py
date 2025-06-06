# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .email_id import EmailId
from .tag import Tag
from .amount import Amount
from .wallet_network import WalletNetwork
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WalletDetails(UniversalBaseModel):
    """
    Standardized model for a Generic wallet transaction
    """

    wallet_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="walletType")] = pydantic.Field(
        default=None
    )
    """
    Wallet type if there are various types of wallets belonging to the same user. E.g. Checking, savings, vault, different currency wallets etc.
    """

    wallet_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="walletId")] = pydantic.Field(
        default=None
    )
    """
    Unique ID of the wallet
    """

    payment_channel: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="paymentChannel")] = (
        pydantic.Field(default=None)
    )
    """
    Payment Channel used through wallet
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the account holder for a specific wallet
    """

    email_id: typing_extensions.Annotated[typing.Optional[EmailId], FieldMetadata(alias="emailId")] = None
    tags: typing.Optional[typing.List[Tag]] = pydantic.Field(default=None)
    """
    Additional information that can be added via tags
    """

    wallet_phone_number: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="walletPhoneNumber")] = (
        pydantic.Field(default=None)
    )
    """
    Phone number associated with the wallet, if any
    """

    wallet_balance: typing_extensions.Annotated[typing.Optional[Amount], FieldMetadata(alias="walletBalance")] = None
    network: typing.Optional[WalletNetwork] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
