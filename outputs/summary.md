# Queens Flooding 311 Analysis Summary

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

- The cleaned dataset contains 50,000 flooding-related 311 records for Queens.
- The ZIP code with the highest complaint count is 11385, with 1,916 complaints.
- The month with the highest complaint count is 2021-09, with 4,292 complaints.
- The most common complaint descriptor is "Sewer Backup (Use Comments) (SA)", with 17,206 complaints.

## Data Quality Notes

The validation process identified:

- 393 records with missing latitude or longitude.
- 236 records with missing ZIP codes.
- 67 records where the closed date appears earlier than the created date.

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
