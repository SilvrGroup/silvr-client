import datetime as dt
from dataclasses import dataclass

import httpx

from .client import Client
from .choices import (
    ExpectedFundingAmountRange,
    DeclaredRevenueRange,
    DeclaredRevenueDuration,
    ApplicationState,
    DocumentCategory,
    Country,
    UploadedFile,
)


@dataclass
class Application:
    uuid: str
    created: dt.datetime
    author: str | None
    state: ApplicationState

    # Contact fields
    first_name: str
    last_name: str
    email: str
    phone_number: str

    # Company fields
    company_name: str
    company_registration_number: str | None
    company_vat_number: str | None
    country: Country

    # Declarative information
    expected_funding_amount_range: ExpectedFundingAmountRange
    declared_monthly_revenue_range: DeclaredRevenueRange
    declared_revenue_duration_range: DeclaredRevenueDuration

    additional_message: str | None

    @classmethod
    def from_request(cls, application_body: dict[str, str | None]) -> "Application":
        application = Application(**application_body)
        application.created = dt.datetime.fromisoformat(application.created)
        application.state = ApplicationState(application.state)
        application.country = Country(application.country)
        application.expected_funding_amount_range = ExpectedFundingAmountRange(
            application.expected_funding_amount_range
        )
        application.declared_monthly_revenue_range = DeclaredRevenueRange(
            application.declared_monthly_revenue_range
        )
        application.declared_revenue_duration_range = DeclaredRevenueDuration(
            application.declared_revenue_duration_range
        )
        return application

    def save(self, client: Client) -> httpx.Response:
        response = client.new_application(
            # Contact
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone_number=self.phone_number,
            # Company
            country=self.country,
            company_name=self.company_name,
            company_registration_number=self.company_registration_number,
            company_vat_number=self.company_vat_number,
            # Application
            expected_funding_amount_range=self.expected_funding_amount_range,
            declared_monthly_revenue_range=self.declared_monthly_revenue_range,
            declared_revenue_duration_range=self.declared_revenue_duration_range,
            # Broker info
            additional_message=self.additional_message,
        )
        body = response.json()
        if "uuid" in body:
            updated_application = Application.from_request(body)
            self.__dict__ = updated_application.__dict__

        return response

    def upload_document(
        self, client: Client, file: UploadedFile, category=DocumentCategory
    ) -> "Document":
        if not self.uuid:
            raise ValueError("Please save your application first")

        return client.new_document(self.uuid, file, category)


@dataclass
class Document:
    uuid: str
    created: dt.datetime
    filename: str
    category: DocumentCategory

    @classmethod
    def from_request(cls, document_body: dict[str, str | None]) -> "Document":
        document = Document(**document_body)
        document.created = dt.datetime.fromisoformat(document.created)
        document.category = DocumentCategory(document.category)
        return document
