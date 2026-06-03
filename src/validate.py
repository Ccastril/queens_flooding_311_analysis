
import pandas as pd

from config import VALIDATION_SUMMARY_PATH


def create_validation_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a summary of data quality checks for the cleaned dataset.
    """
    checks = {
        "total_rows": len(df),
        "missing_created_date": int(df["missing_created_date_flag"].sum()),
        "missing_closed_date": int(df["missing_closed_date_flag"].sum()),
        "missing_zip": int(df["missing_zip_flag"].sum()),
        "missing_location": int(df["missing_location_flag"].sum()),
        "invalid_closed_date": int(df["invalid_closed_date_flag"].sum()),
        "outside_reasonable_nyc_bounds": int(df["outside_reasonable_nyc_bounds_flag"].sum()),
        "duplicate_unique_keys": int(df["duplicate_unique_key_flag"].sum()),
        "usable_for_location_analysis": int(df["usable_for_location_analysis_flag"].sum()),
        "usable_for_time_analysis": int(df["usable_for_time_analysis_flag"].sum()),
    }

    return pd.DataFrame(
        [{"check": key, "count": value} for key, value in checks.items()]
    )


def save_validation_summary(summary_df: pd.DataFrame) -> None:
    VALIDATION_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    summary_df.to_csv(VALIDATION_SUMMARY_PATH, index=False)