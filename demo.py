"""This is a demo of how to use the client to create a new application
and attach documents to it"""
import json
import os
import random
import sys

from silvr_client import choices
from silvr_client import SilvrClient
from silvr_client import TokenAuth
from silvr_client import UploadedFile
from silvr_client.models import Application, Document

API_URL = os.getenv("API_URL", "http://localhost:8000/api/")
BROKER_API_KEY = os.getenv("BROKER_API_KEY", "")
CLIENT_EMAIL = os.getenv("CLIENT_EMAIL", "john.doe11@acme.com")
COMPANY_REGISTRATION_NUMBER = os.getenv("COMPANY_REGISTRATION_NUMBER")


if not BROKER_API_KEY:
    print("Define a BROKER_API_KEY environment variable")
    sys.exit(1)

if not COMPANY_REGISTRATION_NUMBER:
    COMPANY_REGISTRATION_NUMBER = str(random.randint(100000, 1000000))


with SilvrClient(base_url=API_URL, auth=TokenAuth(BROKER_API_KEY)) as client:
    print("List of applications")
    applications_response = client.applications()
    body = applications_response.json()
    print(json.dumps(body, indent=2))
    applications_response.raise_for_status()
    applications = [Application.from_request(a) for a in body]

    existing_application = [
        a
        for a in applications
        if a.email == CLIENT_EMAIL and a.company_registration_number == COMPANY_REGISTRATION_NUMBER
    ]
    application_uuid = None
    if existing_application:
        application_uuid = existing_application[0].uuid

    if not application_uuid:
        print("New application")
        application_response = client.new_application(
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
        body = application_response.json()
        print(json.dumps(body, indent=2))
        application_response.raise_for_status()

        application = Application.from_request(body)
        application_uuid = application.uuid

    print("Add Bank Statement")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("bank_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.BANK_STATEMENT,
    )
    body = document_response.json()
    print(json.dumps(body, indent=2))
    document_response.raise_for_status()
    document = Document.from_request(body)

    print("Add Financial Statement")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("bank_statement.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.FINANCIAL_STATEMENT,
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add Identity Proof")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("cni.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.IDENTITY_PROOF,
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add Proof of Address")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("poa.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.ADDRESS,
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add K_BIS")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("kbis.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.CERTIFICATE_OF_INCORPORATION,
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("Add IBAN")
    document_response = client.new_document(
        application_id=application_uuid,
        file=UploadedFile("iban.pdf", open("demo.pdf", "rb"), choices.ContentType.PDF),
        category=choices.DocumentCategory.IBAN,
    )
    print(json.dumps(document_response.json(), indent=2))
    document_response.raise_for_status()

    print("List of documents")
    documents_response = client.documents(application_id=application_uuid)
    body = documents_response.json()
    print(json.dumps(body, indent=2))
    documents_response.raise_for_status()
    documents = [Document.from_request(d) for d in body]
