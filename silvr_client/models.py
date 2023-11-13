import datetime as dt
from dataclasses import dataclass

from .choices import ExpectedFundingAmountRange, DeclaredRevenueRange, DeclaredRevenueDuration, ApplicationState, DocumentCategory, Country


@dataclass
class Application:
    uuid: str
    created: dt.datetime
    author: str
    
    state: ApplicationState

    # Contact fields
    email: str
    first_name: str
    last_name: str
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
        application.expected_funding_amount_range = ExpectedFundingAmountRange(application.expected_funding_amount_range)
        application.declared_monthly_revenue_range = DeclaredRevenueRange(application.declared_monthly_revenue_range)
        application.declared_revenue_duration_range = DeclaredRevenueDuration(application.declared_revenue_duration_range)
        return application

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

