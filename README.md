# silvr-client

A Python client for brokers to send new applications.

See [demo.py](demo.py) to see how to use the API.


## Install

### From PyPI

```
pip install silvr-client
```

### From source

```
pip install -e .
```

## Demo

```
export BROKER_API_KEY="<api-key>"

CLIENT_EMAIL="john.doe@acme.com" \
COMPANY_REGISTRATION_NUMBER="123456789" \
python demo.py
```

## API

### List existing applications

```python
import os
import httpx
import json

from silvr_client import SilvrClient, TokenAuth
from silvr_client.models import Application, Document

API_URL = "https://demo.silvr.dev/api/"
BROKER_API_KEY = os.getenv("BROKER_API_KEY")

with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    applications_response = client.applications()
    try:
        applications_response.raise_for_status()
    except httpx.HTTPStatusError:
        print(json.dumps(applications_response.json(), indent=2))

    applications = [Application.from_request(a) for a in applications_response.json()]
```

### Create new application

```python
import httpx
import json

from silvr_client import SilvrClient, TokenAuth, choices
from silvr_client.models import Application, Document

COMPANY_REGISTRATION_NUMBER = "123456789"
CLIENT_EMAIL = "john.doe@acme.com"


with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    application = Application(
            first_name="John",
            last_name="Doe",
            email=CLIENT_EMAIL,
            phone_number="+33123456789",
            company_name="ACME SAS",
            company_registration_number=COMPANY_REGISTRATION_NUMBER,
            country=choices.Country.FR,
            expected_funding_amount_range=choices.ExpectedFundingAmountRange.BETWEEN_10K_AND_100K,
            declared_monthly_revenue_range=choices.DeclaredRevenueRange.BETWEEN_10K_AND_25K,
            declared_revenue_duration_range=choices.DeclaredRevenueDuration.ABOVE_12_MONTHS,
            additional_message="API demo",
    )
    application_response = application.save(client)
    try:
        application_response.raise_for_status()
    except httpx.HTTPStatusError:
        print(json.dumps(application_response.json(), indent=2))
    else:
        application = Application.from_request(application_response.json())
```


### Upload a new attachment


```python
import httpx
import json

from silvr_client import SilvrClient, TokenAuth, choices
from silvr_client.models import Application, Document


with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    application = Application.from_request(applications_response.json())

    # From the application object

    document_response = application.upload_document(
        client,
        choices.UploadedFile("bank_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        choices.DocumentCategory.BANK_STATEMENT
    )
    document_response.raise_for_status()
    Document.from_request(document_response.json())

    # Or from the client

    document_response = client.new_document(
        application_id=application.uuid,
        file=choices.UploadedFile("financial_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.FINANCIAL_STATEMENT,
    )
    document_response.raise_for_status()
    Document.from_request(document_response.json())
```


### List all documents


```python
import httpx
import json

from silvr_client import SilvrClient, TokenAuth, choices
from silvr_client.models import Application, Document


with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    documents_response = client.documents(
        application_id=application.uuid,
    )
    documents_response.raise_for_status()
    documents = [Document.from_request(d) for d in documents_response.json()]
```
