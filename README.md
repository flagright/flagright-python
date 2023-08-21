# Flagright Python Library

[![pypi shield](https://img.shields.io/pypi/v/flagright)](https://pypi.org/project/flagright/)

The Flagright Python library provides access to the Flagright API from Python.

## Documentation

API documentation is available at <https://docs.flagright.com>.

## Usage

```python
import flagright
from flagright.client import Flagright


client = Flagright(base_url="https://sandbox.flagright.com", api_key="YOUR_API_KEY")
resposne = client.transactions.verify(request=flagright.Transaction(
    transactionId='my-transaction-id',
    type=flagright.TransactionType.DEPOSIT,
    timestamp=1692624734000))


print(f'Received response from Flagright: "{resposne}"')
```
