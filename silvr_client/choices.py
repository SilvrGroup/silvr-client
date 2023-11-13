import enum
from dataclasses import dataclass
from typing import BinaryIO


class TextChoices(str, enum.Enum):
    pass


class ApplicationState(TextChoices):
    REJECTED = "REJECTED"
    WAITING_FOR_CONNECTORS = "WAITING_FOR_CONNECTORS"
    MISSING_DOCUMENTS = "MISSING_DOCUMENTS"
    EXHAUSTIVITY_CHECK = "EXHAUSTIVITY_CHECK"
    RISK_ANALYSIS = "RISK_ANALYSIS"
    PROPOSITION_SENT = "PROPOSITION_SENT"
    WAITING_FOR_KYB = "WAITING_FOR_KYB"
    KYB_VALIDATION = "KYB_VALIDATION"
    CONTRACT_SENT = "CONTRACT_SENT"
    CONTRACT_SIGNED = "CONTRACT_SIGNED"
    UNKNOWN = "UNKNOWN"


class ExpectedFundingAmountRange(TextChoices):
    LESS_THAN_10K = "LESS_THAN_10K"
    BETWEEN_10K_AND_100K = "BETWEEN_10K_AND_100K"
    MORE_THAN_100K = "MORE_THAN_100K"
    NOT_SURE_YET = "NOT_SURE_YET"


class DeclaredRevenueRange(TextChoices):
    BETWEEN_1K_AND_9K = "BETWEEN_1K_AND_9K"
    BETWEEN_10K_AND_25K = "BETWEEN_10K_AND_25K"
    BETWEEN_25K_AND_50K = "BETWEEN_25K_AND_50K"
    BETWEEN_50K_AND_100K = "BETWEEN_50K_AND_100K"
    BETWEEN_100K_AND_1M = "BETWEEN_100K_AND_1M"


class DeclaredRevenueDuration(TextChoices):
    BETWEEN_1_AND_5_MONTHS = "BETWEEN_1_AND_5_MONTHS"
    BETWEEN_6_AND_11_MONTHS = "BETWEEN_6_AND_11_MONTHS"
    ABOVE_12_MONTHS = "ABOVE_12_MONTHS"


class DocumentCategory(TextChoices):
    # Financial
    BANK_STATEMENT = "BANK_STATEMENT"
    FINANCIAL_STATEMENT = "FINANCIAL_STATEMENT"
    FINANCIAL_UNCATEGORIZED = "FINANCIAL_UNCATEGORIZED"

    # KYB
    IDENTITY_PROOF = "IDENTITY_PROOF"
    ADDRESS = "ADDRESS"
    CERTIFICATE_OF_INCORPORATION = "CERTIFICATE_OF_INCORPORATION"
    IBAN = "IBAN"
    KYB_UNCATEGORIZED = "KYB_UNCATEGORIZED"


class Country(TextChoices):
    FR = "FR"
    DE = "DE"


class ContentType(TextChoices):
    PDF = "application/pdf"


@dataclass
class UploadedFile:
    filename: str
    stream: BinaryIO
    content_type: ContentType

    def astuple(self) -> tuple[str, BinaryIO, ContentType]:
        return (self.filename, self.stream, self.content_type)
