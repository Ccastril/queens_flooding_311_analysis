# Queens Flooding 311 Analysis

A Python ETL and analysis project using NYC Open Data 311 service request records to examine flooding-related complaints in Queens, New York.

This project extracts public 311 complaint data, filters for Queens flooding-related records, cleans and validates the data, creates aggregate summary tables, generates charts, and writes a short findings report.

## Project Question

Where and when are flooding-related 311 complaints concentrated in Queens, and what data quality limitations should analysts consider when using 311 complaint data?

## Motivation

Flooding affects quality of life, infrastructure, transportation, housing, and public safety. Public complaint data can help identify patterns in reported flooding issues, but 311 records are administrative reports rather than direct measurements of flood severity.

This project explores how public administrative data can be cleaned, summarized, and interpreted responsibly.

## Data Source

This project uses NYC Open Data 311 service request records from 2020 to the present.

The extraction query filters for:

* records where `borough = 'QUEENS'`;
* complaint types or descriptors containing flood-related terms;
* selected fields related to complaint timing, location, status, descriptor, and resolution.

The query used for extraction is stored in:

```text
sql/queens_flooding_311_query.sql
```

## Methodology

The project follows a reproducible ETL and analysis workflow:

1. Extract Queens flooding-related 311 records from NYC Open Data.
2. Save the raw dataset.
3. Clean and normalize fields such as dates, ZIP codes, borough names, coordinates, statuses, and descriptors.
4. Create validation flags for missing or questionable records.
5. Aggregate complaint records by ZIP code, month, and complaint descriptor.
6. Generate charts showing complaint patterns.
7. Write a summary report describing findings, data quality notes, and limitations.

## Repository Structure

```text
queens_flooding_311_analysis/
  README.md
  requirements.txt
  .gitignore

  src/
    config.py
    extract.py
    transform.py
    validate.py
    analyze.py
    report.py
    main.py

  sql/
    queens_flooding_311_query.sql

  data/
    raw/
      .gitkeep
    processed/
      .gitkeep

  outputs/
    charts/
      .gitkeep
```

After the pipeline runs, generated files are written to:

```text
data/raw/
data/processed/
outputs/charts/
outputs/summary.md
```

## Outputs

The pipeline produces:

* a raw CSV of extracted 311 records;
* a cleaned CSV with normalized fields and validation flags;
* a validation summary showing missing or questionable values;
* aggregate tables by ZIP code, month, and complaint descriptor;
* charts showing complaint patterns;
* a written summary report.

Expected generated files include:

```text
data/raw/queens_flooding_raw.csv
data/processed/queens_flooding_cleaned.csv
data/processed/queens_flooding_validation_summary.csv
data/processed/queens_flooding_by_zip.csv
data/processed/queens_flooding_by_month.csv
data/processed/queens_flooding_by_descriptor.csv
outputs/charts/complaints_by_zip.png
outputs/charts/complaints_by_month.png
outputs/charts/complaints_by_descriptor.png
outputs/summary.md
```

## Charts

After running the pipeline, the generated charts will appear in `outputs/charts/`.

### Top Queens ZIP Codes by Flooding-Related 311 Complaints

![Top ZIP codes by complaint count](outputs/charts/complaints_by_zip.png)

### Monthly Flooding-Related 311 Complaint Trend

![Monthly complaint trend](outputs/charts/complaints_by_month.png)

### Top Flooding-Related Complaint Descriptors

![Top complaint descriptors](outputs/charts/complaints_by_descriptor.png)

## Data Quality Checks

The cleaning process creates flags for:

* missing created dates;
* missing closed dates;
* missing ZIP codes;
* missing latitude or longitude;
* closed dates that appear earlier than created dates;
* duplicate complaint identifiers;
* coordinates outside broad reasonable NYC bounds;
* records usable for location-based analysis;
* records usable for time-based analysis.

These records are preserved rather than automatically removed so that an analyst can decide how to handle them depending on the research question.

## Limitations

311 complaints are not direct measurements of flooding severity. Complaint volume may reflect actual flooding conditions, but it may also be affected by:

* population density;
* duplicate reports;
* neighborhood-level reporting behavior;
* awareness of 311;
* access to reporting tools;
* agency classification practices;
* differences between reported flooding and actual flood risk.

This project should therefore be interpreted as an analysis of reported flooding-related complaints, not as a complete measure of flood risk, flood damage, or infrastructure failure.

## How to Run

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline from the project root:

```bash
python src/main.py
```

The pipeline will extract data from NYC Open Data, clean and validate the records, create aggregate outputs, generate charts, and write `outputs/summary.md`.

## Main Dependencies

* pandas
* sodapy
* matplotlib

## Relevance

This project demonstrates a concise public-interest data workflow using Python:

* extracting public data from an API;
* separating query logic into a SQL/SoQL file;
* cleaning messy administrative records;
* creating validation and data quality flags;
* producing aggregate analysis outputs;
* generating visualizations;
* communicating findings and limitations clearly.

The project is intended as a code sample for data ETL, analysis, and public-interest investigative analytics work.