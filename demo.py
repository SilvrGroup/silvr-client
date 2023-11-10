"""This is a demo of how to use the client to create a new application and attach documents to it"""
import os
import json
from silvr_client import SilvrClient, TokenAuth, choices, UploadedFile

API_URL = os.getenv("API_URL", "http://localhost:8000/api/")
BROKER_API_KEY = os.getenv("BROKER_API_KEY", "PjvWs8pL96AEJK5jGIZbBKzPbyBJ2kROvzZJqOQUc7TaOyfxoIeAHFfI")


with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    print("List of applications")
    applications_response = client.applications()
    print(json.dumps(applications_response.json(), indent=2))
    applications_response.raise_for_status()

    print("New application")
    application_response = client.new_application(
        first_name="John",
        last_name="Doe",
        email="john5.doe@acme.io",
        phone_number="+33123456789",
        company_name="ACME SAS",
        company_registration_number="924315768",
        country=choices.Country.FR,
        expected_funding_amount_range=choices.ExpectedFundingAmountRange.BETWEEN_10K_AND_100K,
        declared_monthly_revenue_range=choices.DeclaredRevenueRange.BETWEEN_10K_AND_25K,
        declared_revenue_duration_range=choices.DeclaredRevenueDuration.ABOVE_12_MONTHS,
        additional_message = "API demo",
    )
    application = application_response.json()
    print(json.dumps(application, indent=2))
    application_response.raise_for_status()

    print("Add Bank Statement")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("bank_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.BANK_STATEMENT
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add Financial Statement")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("bank_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.FINANCIAL_STATEMENT
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add Identity Proof")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("cni.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.IDENTITY_PROOF
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add Proof of Address")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("poa.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.ADDRESS
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add K_BIS")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("kbis.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.CERTIFICATE_OF_INCORPORATION
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add IBAN")
    document_response = client.new_document(
        application_id=application["uuid"],
        file=UploadedFile("iban.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.IBAN
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("List of documents")
    documents_response = client.documents(application_id=application["uuid"])
    print(json.dumps(documents_response.json(), indent=2))
    documents_response.raise_for_status()
