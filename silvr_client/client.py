import httpx

from .authentication import AuthenticationBackend
from .choices import Country
from .choices import DeclaredRevenueDuration
from .choices import DeclaredRevenueRange
from .choices import DocumentCategory
from .choices import ExpectedFundingAmountRange
from .choices import UploadedFile


class Client(httpx.Client):
    def __init__(
        self, auth: AuthenticationBackend, base_url="https://app.silvr.co/api/", **kwargs
    ) -> None:
        headers = kwargs.get("headers", {})
        headers.update(auth.headers)

        super().__init__(base_url=base_url.rstrip("/"), headers=headers)

    def applications(self) -> httpx.Response:
        return self.get("/v0/brokers/applications")

    def new_application(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        expected_funding_amount_range: ExpectedFundingAmountRange,
        declared_monthly_revenue_range: DeclaredRevenueRange,
        declared_revenue_duration_range: DeclaredRevenueDuration,
        country: Country,
        company_name: str,
        company_registration_number: str = "",
        company_vat_number: str = "",
        additional_message: str = "",
    ) -> httpx.Response:
        return self.post(
            "/v0/brokers/applications",
            json={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_number": phone_number,
                "country": country,
                "company_name": company_name,
                "company_registration_number": company_registration_number,
                "company_vat_number": company_vat_number,
                "expected_funding_amount_range": expected_funding_amount_range,
                "declared_monthly_revenue_range": declared_monthly_revenue_range,
                "declared_revenue_duration_range": declared_revenue_duration_range,
                "additional_message": additional_message,
            },
        )

    def documents(self, application_id: str) -> httpx.Response:
        return self.get(f"/v0/brokers/applications/{application_id}/documents")

    def new_document(
        self, application_id: str, file: UploadedFile, category: DocumentCategory
    ) -> httpx.Response:
        data = {"category": category.value}
        files = {"file": file.astuple()}
        return self.post(
            f"/v0/brokers/applications/{application_id}/documents", data=data, files=files
        )
