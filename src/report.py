import pandas as pd

from config import SUMMARY_MD_PATH


def create_summary_report(
    cleaned_df: pd.DataFrame,
    by_zip: pd.DataFrame,
    by_month: pd.DataFrame,
    by_descriptor: pd.DataFrame,
    validation_summary: pd.DataFrame,
) -> str:
    total_rows = len(cleaned_df)

    top_zip = by_zip.iloc[0]
    top_month = by_month.sort_values("complaint_count", ascending=False).iloc[0]
    top_descriptor = by_descriptor.iloc[0]

    missing_location_count = int(
        validation_summary.loc[
            validation_summary["check"] == "missing_location", "count"
        ].iloc[0]
    )

    missing_zip_count = int(
        validation_summary.loc[
            validation_summary["check"] == "missing_zip", "count"
        ].iloc[0]
    )

    invalid_closed_date_count = int(
        validation_summary.loc[
            validation_summary["check"] == "invalid_closed_date", "count"
        ].iloc[0]
    )

    return f"""# Queens Flooding 311 Analysis Summary

## Project Question

Where and when are flooding-related 311 complaints concentrated in Queens, and what data quality limitations should analysts consider when using 311 complaint data?

## Data Source

This analysis uses NYC Open Data 311 service request records from 2020 to the present. The pipeline filters for Queens records related to flooding, sewer, and flood-related complaint descriptors.

## Methodology

The project follows a reproducible ETL and analysis workflow:

1. Extract flooding-related 311 records for Queens.
2. Clean and normalize date, ZIP code, borough, status, descriptor, and coordinate fields.
3. Create validation flags for missing dates, missing ZIP codes, missing coordinates, invalid closed dates, duplicate complaint IDs, and coordinates outside reasonable NYC bounds.
4. Aggregate complaint records by ZIP code, month, and complaint descriptor.
5. Export cleaned datasets, validation summaries, aggregate tables, and charts.

## Key Findings

- The cleaned dataset contains {total_rows:,} flooding-related 311 records for Queens.
- The ZIP code with the highest complaint count is {top_zip["incident_zip"]}, with {int(top_zip["complaint_count"]):,} complaints.
- The month with the highest complaint count is {top_month["year_month"]}, with {int(top_month["complaint_count"]):,} complaints.
- The most common complaint descriptor is "{top_descriptor["descriptor"]}", with {int(top_descriptor["complaint_count"]):,} complaints.

## Data Quality Notes

The validation process identified:

- {missing_location_count:,} records with missing latitude or longitude.
- {missing_zip_count:,} records with missing ZIP codes.
- {invalid_closed_date_count:,} records where the closed date appears earlier than the created date.

These records were preserved in the cleaned dataset and flagged so analysts can decide whether to include or exclude them depending on the analysis.

## Limitations

311 complaints are administrative reports, not direct measurements of flooding severity. Complaint volume may reflect actual flooding conditions, but it may also be influenced by population density, duplicate reporting, awareness of 311, access to reporting tools, agency classification practices, and neighborhood-level reporting behavior.

This analysis should therefore be interpreted as a study of reported flooding-related complaints, not as a complete measure of flood risk or flood damage.

## Outputs

The project produces:

- `data/raw/queens_flooding_raw.csv`
- `data/processed/queens_flooding_cleaned.csv`
- `data/processed/queens_flooding_validation_summary.csv`
- `data/processed/queens_flooding_by_zip.csv`
- `data/processed/queens_flooding_by_month.csv`
- `data/processed/queens_flooding_by_descriptor.csv`
- `outputs/charts/complaints_by_zip.png`
- `outputs/charts/complaints_by_month.png`
- `outputs/charts/complaints_by_descriptor.png`

## Relevance

This project demonstrates a concise public-interest data workflow using Python: extracting public data, cleaning messy administrative records, creating validation flags, producing aggregate outputs, and communicating findings and limitations clearly.
"""


def save_summary_report(report: str) -> None:
    SUMMARY_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_MD_PATH.write_text(report, encoding="utf-8")