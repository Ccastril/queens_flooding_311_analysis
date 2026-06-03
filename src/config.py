from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATASET_ID = "erm2-nwe9"
DOMAIN = "data.cityofnewyork.us"

QUERY_SQL_PATH = PROJECT_ROOT / "sql" / "queens_flooding_311_query.sql"
QUERY_LIMIT = 50000


RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "queens_flooding_raw.csv"
CLEANED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "queens_flooding_cleaned.csv"
ZIP_SUMMARY_PATH = PROJECT_ROOT / "data" / "processed" / "queens_flooding_by_zip.csv"
MONTH_SUMMARY_PATH = PROJECT_ROOT / "data" / "processed" / "queens_flooding_by_month.csv"
VALIDATION_SUMMARY_PATH = PROJECT_ROOT / "data" / "processed" / "queens_flooding_validation_summary.csv"
DESCRIPTOR_SUMMARY_PATH = PROJECT_ROOT / "data" / "processed" / "queens_flooding_by_descriptor.csv"


CHARTS_DIR = PROJECT_ROOT / "outputs" / "charts"
ZIP_CHART_PATH = CHARTS_DIR / "complaints_by_zip.png"
MONTH_CHART_PATH = CHARTS_DIR / "complaints_by_month.png"
DESCRIPTOR_CHART_PATH = CHARTS_DIR / "complaints_by_descriptor.png"

SUMMARY_MD_PATH = PROJECT_ROOT / "outputs" / "summary.md"