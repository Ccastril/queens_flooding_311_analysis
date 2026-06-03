import pandas as pd
from config import CLEANED_DATA_PATH

def clean_flooding_records(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and validate Queens flooding-related 311 records.

    This function preserves the original complaint records while adding
    standardized fields and data quality flags used for analysis.
    """
    cleaned = df.copy()

    # Standardize column names just in case Socrata returns inconsistent casing.
    cleaned.columns = cleaned.columns.str.strip().str.lower()

    # Parse date fields.
    cleaned["created_date"] = pd.to_datetime(cleaned["created_date"], errors="coerce")
    cleaned["closed_date"] = pd.to_datetime(cleaned["closed_date"], errors="coerce")

    # Normalize text fields.
    text_columns = [
        "agency",
        "complaint_type",
        "descriptor",
        "borough",
        "status",
        "resolution_description",
    ]

    for column in text_columns:
        if column in cleaned.columns:
            cleaned[column] = (
                cleaned[column]
                .astype("string")
                .str.strip()
            )

    # Normalize borough.
    cleaned["borough"] = cleaned["borough"].str.upper()

    # Extract valid 5-digit ZIP codes.
    cleaned["incident_zip"] = (
        cleaned["incident_zip"]
        .astype("string")
        .str.extract(r"(\d{5})")[0]
    )

    # Convert coordinates to numeric values.
    cleaned["latitude"] = pd.to_numeric(cleaned["latitude"], errors="coerce")
    cleaned["longitude"] = pd.to_numeric(cleaned["longitude"], errors="coerce")

    # Create time fields for aggregation.
    cleaned["year"] = cleaned["created_date"].dt.year
    cleaned["year_month"] = cleaned["created_date"].dt.to_period("M").astype("string")

    # Calculate days to close.
    cleaned["days_to_close"] = (
        cleaned["closed_date"] - cleaned["created_date"]
    ).dt.total_seconds() / 86400

    # Data quality flags.
    cleaned["missing_created_date_flag"] = cleaned["created_date"].isna()
    cleaned["missing_closed_date_flag"] = cleaned["closed_date"].isna()
    cleaned["missing_zip_flag"] = cleaned["incident_zip"].isna()
    cleaned["missing_location_flag"] = cleaned["latitude"].isna() | cleaned["longitude"].isna()
    cleaned["invalid_closed_date_flag"] = cleaned["closed_date"] < cleaned["created_date"]

    # Queens coordinate sanity check.
    cleaned["outside_reasonable_nyc_bounds_flag"] = (
        (cleaned["latitude"] < 40.45)
        | (cleaned["latitude"] > 40.95)
        | (cleaned["longitude"] < -74.30)
        | (cleaned["longitude"] > -73.65)
    )

    # Duplicate complaint ID flag.
    cleaned["duplicate_unique_key_flag"] = cleaned.duplicated(
        subset=["unique_key"],
        keep=False
    )

    # Analysis usability flag.
    cleaned["usable_for_location_analysis_flag"] = (
        ~cleaned["missing_location_flag"]
        & ~cleaned["outside_reasonable_nyc_bounds_flag"]
    )

    cleaned["usable_for_time_analysis_flag"] = ~cleaned["missing_created_date_flag"]

    return cleaned

def save_cleaned_data(df: pd.DataFrame) -> None:
    CLEANED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(CLEANED_DATA_PATH, index=False)
