# Reference
## Transactions
<details><summary><code>client.transactions.<a href="src/flagright/transactions/client.py">verify</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Transactions

`/transactions` endpoint allows you to operate on the [Transaction entity.](/guides/overview/entities#transaction)

In order to pass the payload of a transaction to Flagright and verify the transaction, you will need to call this endpoint with the transaction payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.


### Payload

Here are some of the most used payload fields explained (you can find the full payload [schema below](/api-reference/api-reference/transactions/verify#request) with 1 line descriptions):

* `type`: Type of transaction (Ex: `WITHDRAWAL`, `DEPOSIT`, `TRANSFER` etc).
* `transactionId` - Unique Identifier for the transaction.
* `timestamp` - UNIX timestamp in *milliseconds* of when the transaction took place
* `transactionState` - The state of the transaction, set to `CREATED` by default. [More details here](/guides/overview/entities#transaction-lifecycle-through-transaction-events)
* `originUserId` - Unique identifier (if any) of the user who is sending the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
* `destinationUserId` - Unique identifier (if any) of the user who is receiving the money. This user must be created within the Flagright system before using the [create a consumer user](/api-reference/api-reference/consumer-users/create) or [create a business user](/api-reference/api-reference/business-users/create) endpoint
* `originAmountDetails` - Details of the amount being sent from the origin
* `destinationAmountDetails` - Details of the amount being received at the destination
* `originPaymentDetails` - Payment details (if any) used at the origin (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
* `destinationPaymentDetails` - Payment details (if any) used at the destination (ex: `CARD`, `IBAN`, `WALLET` etc). You can click on the dropdown next to the field in the schema below to view all supported payment types.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import (
    DeviceData,
    Flagright,
    Tag,
    TransactionAmountDetails,
    TransactionDestinationPaymentDetails_Card,
    TransactionOriginPaymentDetails_Card,
)

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.transactions.verify(
    type="DEPOSIT",
    transaction_id="7b80a539eea6e78acbd6d458e5971482",
    timestamp=1641654664000.0,
    origin_user_id="8650a2611d0771cba03310f74bf6",
    destination_user_id="9350a2611e0771cba03310f74bf6",
    origin_amount_details=TransactionAmountDetails(
        transaction_amount=800.0,
        transaction_currency="EUR",
        country="DE",
    ),
    destination_amount_details=TransactionAmountDetails(
        transaction_amount=68351.34,
        transaction_currency="INR",
        country="IN",
    ),
    origin_payment_details=TransactionOriginPaymentDetails_Card(
        card_fingerprint="20ac00fed8ef913aefb17cfae1097cce",
        card_issued_country="TR",
        transaction_reference_field="Deposit",
        f_3_ds_done=True,
    ),
    destination_payment_details=TransactionDestinationPaymentDetails_Card(
        card_fingerprint="20ac00fed8ef913aefb17cfae1097cce",
        card_issued_country="TR",
        transaction_reference_field="Deposit",
        f_3_ds_done=True,
    ),
    promotion_code_used=True,
    reference="loan repayment",
    origin_device_data=DeviceData(
        battery_level=95.0,
        device_latitude=13.0033,
        device_longitude=76.1004,
        ip_address="10.23.191.2",
        device_identifier="3c49f915d04485e34caba",
        vpn_used=False,
        operating_system="Android 11.2",
        device_maker="ASUS",
        device_model="Zenphone M2 Pro Max",
        device_year="2018",
        app_version="1.1.0",
    ),
    destination_device_data=DeviceData(
        battery_level=95.0,
        device_latitude=13.0033,
        device_longitude=76.1004,
        ip_address="10.23.191.2",
        device_identifier="3c49f915d04485e34caba",
        vpn_used=False,
        operating_system="Android 11.2",
        device_maker="ASUS",
        device_model="Zenphone M2 Pro Max",
        device_year="2018",
        app_version="1.1.0",
    ),
    tags=[
        Tag(
            key="customKey",
            value="customValue",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `str` — Type of transaction (ex: DEPOSIT, WITHDRAWAL, TRANSFER, EXTERNAL_PAYMENT, REFUND, OTHER)
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — Unique transaction identifier
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `float` — Timestamp of when transaction took place
    
</dd>
</dl>

<dl>
<dd>

**validate_origin_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate if provided originUserId exist. True by default
    
</dd>
</dl>

<dl>
<dd>

**validate_destination_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate if provided destinationUserId exist. True by default
    
</dd>
</dl>

<dl>
<dd>

**origin_user_id:** `typing.Optional[str]` — UserId for where the transaction originates from
    
</dd>
</dl>

<dl>
<dd>

**destination_user_id:** `typing.Optional[str]` — UserId for transaction's destination. In other words, where the value is being transferred to.
    
</dd>
</dl>

<dl>
<dd>

**transaction_state:** `typing.Optional[TransactionState]` 
    
</dd>
</dl>

<dl>
<dd>

**origin_amount_details:** `typing.Optional[TransactionAmountDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_amount_details:** `typing.Optional[TransactionAmountDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**origin_payment_details:** `typing.Optional[TransactionOriginPaymentDetails]` — Payment details of the origin. It can be a bank account number, wallet ID, card fingerprint etc.
    
</dd>
</dl>

<dl>
<dd>

**destination_payment_details:** `typing.Optional[TransactionDestinationPaymentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**origin_funds_info:** `typing.Optional[OriginFundsInfo]` 
    
</dd>
</dl>

<dl>
<dd>

**related_transaction_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of transactions related to this transaction. Ex: refund, split bills
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[str]` — Type of produce being used by the consumer (ex wallets, payments etc)
    
</dd>
</dl>

<dl>
<dd>

**promotion_code_used:** `typing.Optional[bool]` — Whether a promotion code was used or not the transaction
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Reference field for the transaction indicating the purpose of the transaction etc.
    
</dd>
</dl>

<dl>
<dd>

**origin_device_data:** `typing.Optional[DeviceData]` 
    
</dd>
</dl>

<dl>
<dd>

**destination_device_data:** `typing.Optional[DeviceData]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[Tag]]` — Additional information that can be added via tags
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transactions.<a href="src/flagright/transactions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET Transactions

`/transactions` endpoint allows you to operate on the [Transaction entity](/guides/overview/entities#transaction).

Calling `GET /transactions/{transactionId}` will return the entire transaction payload and rule execution results for the transaction with the corresponding `transactionId`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.transactions.get(
    transaction_id="transactionId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transaction_id:** `str` — Unique Transaction Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Batch
<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">verify_transaction</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright, Transaction

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.verify_transaction(
    data=[
        Transaction(
            type="type",
            transaction_id="transactionId",
            timestamp=1.1,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[Transaction]` 
    
</dd>
</dl>

<dl>
<dd>

**validate_origin_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate if provided originUserId exist. True by default
    
</dd>
</dl>

<dl>
<dd>

**validate_destination_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate if provided destinationUserId exist. True by default
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.get(
    batch_id="batchId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**batch_id:** `str` — Unique Batch Identifier
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[PageSize]` — Page size (default 20)
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[Page]` — Page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">create_transaction_events</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright, TransactionEvent

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.create_transaction_events(
    data=[
        TransactionEvent(
            transaction_state="CREATED",
            timestamp=1.1,
            transaction_id="transactionId",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[TransactionEvent]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">create_consumer_users</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright, User

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.create_consumer_users(
    data=[
        User(
            user_id="userId",
            created_timestamp=1.1,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[User]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">create_business_users</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Business, CompanyGeneralDetails, Flagright, LegalEntity

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.create_business_users(
    data=[
        Business(
            user_id="userId",
            created_timestamp=1.1,
            legal_entity=LegalEntity(
                company_general_details=CompanyGeneralDetails(
                    legal_name="Ozkan Hazelnut Export JSC",
                    business_industry=["Farming"],
                    main_products_services_sold=["Hazelnut"],
                ),
            ),
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[Business]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">create_consumer_user_events</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import ConsumerUserEvent, Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.create_consumer_user_events(
    data=[
        ConsumerUserEvent(
            timestamp=1.1,
            user_id="userId",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[ConsumerUserEvent]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.batch.<a href="src/flagright/batch/client.py">create_business_user_events</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import BusinessUserEvent, Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.batch.create_business_user_events(
    data=[
        BusinessUserEvent(
            timestamp=1.1,
            user_id="userId",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `typing.Sequence[BusinessUserEvent]` 
    
</dd>
</dl>

<dl>
<dd>

**batch_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TransactionEvents
<details><summary><code>client.transaction_events.<a href="src/flagright/transaction_events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Transaction Events

`/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](/guides/overview/entities#transaction-event)

Transaction events are created after the initial `POST /transactions` call (which creates a transaction) and are used to:

* Update the STATE of the transaction, using the `transactionState` field and manage the [Transaction Lifecycle](/guides/overview/entities#transaction-lifecycle-through-transaction-events)
* Update the transaction details, using the `updatedTransactionAttributes` field.

> If you have neither of the above two use cases, you do not need to use transaction events.

### Payload

Each transaction event needs three mandatory fields:

* `transactionState` - STATE of the transaction -> value is set to `CREATED` after `POST /transactions` call
* `timestamp`- the timestamp of when the event was created or occured in your system
* `transactionId` - The ID of the transaction for which this event is generated.

In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import DeviceData, Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.transaction_events.create(
    transaction_state="SUCCESSFUL",
    timestamp=1752526580000.0,
    transaction_id="443dea26147a406b957d9ee3a1247b11",
    event_id="aaeeb166147a406b957dd9147a406b957",
    event_description="Transaction created",
    meta_data=DeviceData(
        battery_level=76.3,
        device_latitude=13.009711,
        device_longitude=76.102898,
        ip_address="79.144.2.20",
        vpn_used=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transaction_state:** `TransactionState` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp:** `float` — Timestamp of the event
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `str` — Transaction ID the event pertains to
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` — Unique event ID
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Reason for the event or a state change
    
</dd>
</dl>

<dl>
<dd>

**event_description:** `typing.Optional[str]` — Event description
    
</dd>
</dl>

<dl>
<dd>

**updated_transaction_attributes:** `typing.Optional[TransactionUpdatable]` 
    
</dd>
</dl>

<dl>
<dd>

**meta_data:** `typing.Optional[DeviceData]` 
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transaction_events.<a href="src/flagright/transaction_events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET Transaction Events

`/events/transaction` endpoint allows you to operate on the [Transaction Events entity.](/guides/overview/entities#transaction-event).

You can retrieve any transaction event you created using the [POST Transaction Events](/api-reference/api-reference/transaction-events/create) call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.transaction_events.get(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Unique Transaction Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConsumerUsers
<details><summary><code>client.consumer_users.<a href="src/flagright/consumer_users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Consumer User

`/consumer/user` endpoint allows you to operate on the Consumer user entity.

In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

### Payload

Each consumer user needs two mandatory fields:

* `userId` - Unique identifier for the user
* `createdTimestamp` - UNIX timestamp in *milliseconds* for when the User is created in your system
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import (
    Address,
    ConsumerName,
    ContactDetails,
    Flagright,
    LegalDocument,
    Tag,
    UserDetails,
    UserTag,
)

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.consumer_users.create(
    user_id="96647cfd9e8fe66ee0f3362e011e34e8",
    created_timestamp=1641654664000.0,
    user_details=UserDetails(
        name=ConsumerName(
            first_name="Baran",
            middle_name="Realblood",
            last_name="Ozkan",
        ),
        date_of_birth="1991-01-01",
        country_of_residence="US",
        country_of_nationality="DE",
    ),
    legal_documents=[
        LegalDocument(
            document_type="passport",
            document_number="Z9431P",
            document_issued_date=1639939034000.0,
            document_expiration_date=1839939034000.0,
            document_issued_country="DE",
            tags=[
                Tag(
                    key="customerType",
                    value="wallet",
                )
            ],
        )
    ],
    contact_details=ContactDetails(
        email_ids=["baran@flagright.com"],
        contact_numbers=["+37112345432"],
        websites=["flagright.com"],
        addresses=[
            Address(
                address_lines=["Klara-Franke Str 20"],
                postcode="10557",
                city="Berlin",
                state="Berlin",
                country="Germany",
                tags=[
                    Tag(
                        key="customKey",
                        value="customValue",
                    )
                ],
            )
        ],
    ),
    tags=[
        UserTag(
            key="customKey",
            value="customValue",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Unique user ID
    
</dd>
</dl>

<dl>
<dd>

**created_timestamp:** `float` — Timestamp when userId is created
    
</dd>
</dl>

<dl>
<dd>

**lock_cra_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the CRA risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**lock_kyc_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the KYC risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**validate_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate the userId
    
</dd>
</dl>

<dl>
<dd>

**activated_timestamp:** `typing.Optional[float]` — Timestamp when user was activated
    
</dd>
</dl>

<dl>
<dd>

**user_details:** `typing.Optional[UserDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**user_state_details:** `typing.Optional[UserStateDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**kyc_status_details:** `typing.Optional[KycStatusDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**eodd_date:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_status:** `typing.Optional[EmploymentStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**occupation:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**legal_documents:** `typing.Optional[typing.Sequence[LegalDocument]]` — User's legal identity documents - See Document Model for details
    
</dd>
</dl>

<dl>
<dd>

**contact_details:** `typing.Optional[ContactDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**employment_details:** `typing.Optional[EmploymentDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_limits:** `typing.Optional[TransactionLimits]` 
    
</dd>
</dl>

<dl>
<dd>

**expected_income:** `typing.Optional[ExpectedIncome]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_level:** `typing.Optional[RiskLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**kyc_risk_level:** `typing.Optional[RiskLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**acquisition_channel:** `typing.Optional[AcquisitionChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**reason_for_account_opening:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**source_of_funds:** `typing.Optional[typing.Sequence[SourceOfFunds]]` 
    
</dd>
</dl>

<dl>
<dd>

**user_segment:** `typing.Optional[ConsumerUserSegment]` 
    
</dd>
</dl>

<dl>
<dd>

**pep_status:** `typing.Optional[typing.Sequence[PepStatus]]` 
    
</dd>
</dl>

<dl>
<dd>

**sanctions_status:** `typing.Optional[SanctionsStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**adverse_media_status:** `typing.Optional[AdverseMediaStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**last_transaction_timestamp:** `typing.Optional[float]` — Timestamp of the last successful transaction of the user
    
</dd>
</dl>

<dl>
<dd>

**linked_entities:** `typing.Optional[UserEntityLink]` 
    
</dd>
</dl>

<dl>
<dd>

**saved_payment_details:** `typing.Optional[typing.Sequence[UserSavedPaymentDetailsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[UserTag]]` — Additional information that can be added via tags
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[PersonAttachment]]` — Uploaded user's attachment
    
</dd>
</dl>

<dl>
<dd>

**meta_data:** `typing.Optional[DeviceData]` 
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consumer_users.<a href="src/flagright/consumer_users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET Consumer User

`/consumer/user` endpoint allows you to operate on the Consumer User entity.

Calling `GET /consumer/user/{userId}` will return the entire user payload and rule execution results for the user with the corresponding `userId`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.consumer_users.get(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BusinessUsers
<details><summary><code>client.business_users.<a href="src/flagright/business_users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Business User

`/business/user` endpoint allows you to operate on the Business user entity.

In order to pass the payload of a User to Flagright and verify the User, you will need to call this endpoint with the User payload. Not all fields are mandatory, you will only need to pass in the fields that you have and are relevant for your compliance setup.

### Payload


Each business user needs three mandatory fields:

* `userId` - Unique identifier for the user
* `legalEntity` - Details of the business legal entity (CompanyGeneralDetails, FinancialDetails etc) - only `legalName`in `CompanyGeneralDetails` is mandatory
* `createdTimestamp` - UNIX timestamp in *milliseconds* for when the User is created in your system
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import CompanyGeneralDetails, Flagright, LegalEntity

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.business_users.create(
    user_id="userId",
    created_timestamp=1.1,
    legal_entity=LegalEntity(
        company_general_details=CompanyGeneralDetails(
            legal_name="Ozkan Hazelnut Export JSC",
            business_industry=["Farming"],
            main_products_services_sold=["Hazelnut"],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — Unique user ID for the user
    
</dd>
</dl>

<dl>
<dd>

**created_timestamp:** `float` — Timestamp when the user was created
    
</dd>
</dl>

<dl>
<dd>

**legal_entity:** `LegalEntity` 
    
</dd>
</dl>

<dl>
<dd>

**lock_cra_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the CRA risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**lock_kyc_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the KYC risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**validate_user_id:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should validate the userId
    
</dd>
</dl>

<dl>
<dd>

**activated_timestamp:** `typing.Optional[float]` — Timestamp when the user was activated
    
</dd>
</dl>

<dl>
<dd>

**user_state_details:** `typing.Optional[UserStateDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**kyc_status_details:** `typing.Optional[KycStatusDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**share_holders:** `typing.Optional[typing.Sequence[Person]]` — Shareholders (beneficiaries) of the company that hold at least 25% ownership. Can be another company or an individual
    
</dd>
</dl>

<dl>
<dd>

**directors:** `typing.Optional[typing.Sequence[Person]]` — Director(s) of the company. Must be at least one
    
</dd>
</dl>

<dl>
<dd>

**transaction_limits:** `typing.Optional[TransactionLimits]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_level:** `typing.Optional[RiskLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**kyc_risk_level:** `typing.Optional[RiskLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_payment_methods:** `typing.Optional[typing.Sequence[PaymentMethod]]` 
    
</dd>
</dl>

<dl>
<dd>

**last_transaction_timestamp:** `typing.Optional[float]` — Timestamp of the last successful transaction of the user
    
</dd>
</dl>

<dl>
<dd>

**linked_entities:** `typing.Optional[UserEntityLink]` 
    
</dd>
</dl>

<dl>
<dd>

**acquisition_channel:** `typing.Optional[AcquisitionChannel]` 
    
</dd>
</dl>

<dl>
<dd>

**saved_payment_details:** `typing.Optional[typing.Sequence[BusinessSavedPaymentDetailsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**mcc_details:** `typing.Optional[MccDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[UserTag]]` — Additional information that can be added via tags
    
</dd>
</dl>

<dl>
<dd>

**attachments:** `typing.Optional[typing.Sequence[PersonAttachment]]` — User's attachments uploaded by business user
    
</dd>
</dl>

<dl>
<dd>

**meta_data:** `typing.Optional[DeviceData]` 
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.business_users.<a href="src/flagright/business_users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET Business User

`/business/user` endpoint allows you to operate on the Business User entity.

Calling `GET /business/user/{userId}` will return the entire User payload and rule execution results for the User with the corresponding `userId`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.business_users.get(
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_id:** `str` — 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConsumerUserEvents
<details><summary><code>client.consumer_user_events.<a href="src/flagright/consumer_user_events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Consumer User Events

`/events/consumer/user` endpoint allows you to operate on the Consumer User Events entity.

User events are created after the initial `POST /consumer/users` call (which creates a user) and are used to:

* Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
* Update the user details, using the `updatedConsumerUserAttributes` field.

> If you have neither of the above two use cases, you do not need to use user events.

### Payload

Each user event needs three mandatory fields:

* `timestamp`- the timestamp of when the event was created or occured in your system
* `userId` - The ID of the transaction for which this event is generated.

In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.consumer_user_events.create(
    timestamp=1.1,
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**timestamp:** `float` — Timestamp of the event
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Transaction ID the event pertains to
    
</dd>
</dl>

<dl>
<dd>

**allow_user_type_conversion:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should allow a Consumer user event to be applied to a Business user with the same user ID. This will converts a Business user to a Consumer user.
    
</dd>
</dl>

<dl>
<dd>

**lock_kyc_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the KYC risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**lock_cra_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the CRA risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` — Unique event ID
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Reason for the event or a state change
    
</dd>
</dl>

<dl>
<dd>

**event_description:** `typing.Optional[str]` — Event description
    
</dd>
</dl>

<dl>
<dd>

**updated_consumer_user_attributes:** `typing.Optional[UserOptional]` 
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.consumer_user_events.<a href="src/flagright/consumer_user_events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET a Consumer User Event
You can retrieve any consumer user event you created using the [POST Consumer User Events](/api-reference/api-reference/consumer-user-events/create) call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.consumer_user_events.get(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Unique Consumer User Event Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BusinessUserEvents
<details><summary><code>client.business_user_events.<a href="src/flagright/business_user_events/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

## POST Business User Events

`/events/business/user` endpoint allows you to operate on the Business User Events entity.

User events are created after the initial `POST /business/users` call (which creates a user) and are used to:

* Update the STATE and KYC Status of the user, using the `userStateDetails` or `kycStatusDetails` field
* Update the user details, using the `updatedBusinessUserAttributes` field.

> If you have neither of the above two use cases, you do not need to use user events.

### Payload

Each user event needs three mandatory fields:

* `timestamp`- the timestamp of when the event was created or occured in your system
* `userId` - The ID of the transaction for which this event is generated.

In order to make individual events retrievable, you also need to pass in a unique `eventId` to the request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.business_user_events.create(
    timestamp=1.1,
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**timestamp:** `float` — Timestamp of the event
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `str` — Transaction ID the event pertains to
    
</dd>
</dl>

<dl>
<dd>

**allow_user_type_conversion:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should allow a Business user event to be applied to a Consumer user with the same user ID. This will converts a Consumer user to a Business user.
    
</dd>
</dl>

<dl>
<dd>

**lock_kyc_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the KYC risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**lock_cra_risk_level:** `typing.Optional[BooleanString]` — Boolean string whether Flagright should lock the CRA risk level for the user.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` — Unique event ID
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Reason for the event or a state change
    
</dd>
</dl>

<dl>
<dd>

**event_description:** `typing.Optional[str]` — Event description
    
</dd>
</dl>

<dl>
<dd>

**updated_business_user_attributes:** `typing.Optional[BusinessOptional]` 
    
</dd>
</dl>

<dl>
<dd>

**update_count:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.business_user_events.<a href="src/flagright/business_user_events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

### GET a Business User Event
You can retrieve any business user event you created using the [POST Business User Events](/api-reference/api-reference/business-user-events/create) call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from flagright import Flagright

client = Flagright(
    api_key="YOUR_API_KEY",
)
client.business_user_events.get(
    event_id="eventId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — Unique Business User Event Identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

