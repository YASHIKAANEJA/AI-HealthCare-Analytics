import re


# Column names that may contain sensitive information
PII_PATTERNS = {
    "Patient Name": r"\b(patient|person|first|last|full)[ _-]*name\b|\bname\b",
    "Email Address": r"\bemail([ _-]*address)?\b|\be[ _-]*mail\b",
    "Phone Number": r"\b(phone|telephone|mobile|contact)[ _-]*(number|no)?\b|\bphone\b",
    "Date of Birth": r"\b(date[ _-]*of[ _-]*birth|dob|birth[ _-]*date)\b",
    "Medical Record Number": r"\b(mrn|medical[ _-]*record[ _-]*(number|no|id))\b",
    "Patient Identifier": r"\b(patient[ _-]*(id|identifier|number|no))\b",
    "Address": r"\b(home[ _-]*)?address\b|\bstreet[ _-]*address\b",
    "Social Security Number": r"\b(ssn|social[ _-]*security[ _-]*(number|no))\b",
}


def detect_sensitive_columns(columns):
    """Return columns whose names suggest potentially sensitive data."""

    flagged_columns = []

    for column in columns:
        normalized = re.sub(r"[_-]+", " ", str(column).strip().lower())

        for category, pattern in PII_PATTERNS.items():
            if re.search(pattern, normalized, re.IGNORECASE):
                flagged_columns.append({
                    "column": str(column),
                    "category": category
                })
                break

    return flagged_columns