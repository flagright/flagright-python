# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import FlagrightEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .transactions.client import TransactionsClient
from .batch.client import BatchClient
from .transaction_events.client import TransactionEventsClient
from .consumer_users.client import ConsumerUsersClient
from .business_users.client import BusinessUsersClient
from .consumer_user_events.client import ConsumerUserEventsClient
from .business_user_events.client import BusinessUserEventsClient
from .core.client_wrapper import AsyncClientWrapper
from .transactions.client import AsyncTransactionsClient
from .batch.client import AsyncBatchClient
from .transaction_events.client import AsyncTransactionEventsClient
from .consumer_users.client import AsyncConsumerUsersClient
from .business_users.client import AsyncBusinessUsersClient
from .consumer_user_events.client import AsyncConsumerUserEventsClient
from .business_user_events.client import AsyncBusinessUserEventsClient


class Flagright:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FlagrightEnvironment
        The environment to use for requests from the client. from .environment import FlagrightEnvironment



        Defaults to FlagrightEnvironment.SANDBOX_API_SERVER_EU_1



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from flagright import Flagright

    client = Flagright(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FlagrightEnvironment = FlagrightEnvironment.SANDBOX_API_SERVER_EU_1,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.transactions = TransactionsClient(client_wrapper=self._client_wrapper)
        self.batch = BatchClient(client_wrapper=self._client_wrapper)
        self.transaction_events = TransactionEventsClient(client_wrapper=self._client_wrapper)
        self.consumer_users = ConsumerUsersClient(client_wrapper=self._client_wrapper)
        self.business_users = BusinessUsersClient(client_wrapper=self._client_wrapper)
        self.consumer_user_events = ConsumerUserEventsClient(client_wrapper=self._client_wrapper)
        self.business_user_events = BusinessUserEventsClient(client_wrapper=self._client_wrapper)


class AsyncFlagright:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FlagrightEnvironment
        The environment to use for requests from the client. from .environment import FlagrightEnvironment



        Defaults to FlagrightEnvironment.SANDBOX_API_SERVER_EU_1



    api_key : str
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from flagright import AsyncFlagright

    client = AsyncFlagright(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FlagrightEnvironment = FlagrightEnvironment.SANDBOX_API_SERVER_EU_1,
        api_key: str,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.transactions = AsyncTransactionsClient(client_wrapper=self._client_wrapper)
        self.batch = AsyncBatchClient(client_wrapper=self._client_wrapper)
        self.transaction_events = AsyncTransactionEventsClient(client_wrapper=self._client_wrapper)
        self.consumer_users = AsyncConsumerUsersClient(client_wrapper=self._client_wrapper)
        self.business_users = AsyncBusinessUsersClient(client_wrapper=self._client_wrapper)
        self.consumer_user_events = AsyncConsumerUserEventsClient(client_wrapper=self._client_wrapper)
        self.business_user_events = AsyncBusinessUserEventsClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FlagrightEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
