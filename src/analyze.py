import pandas as pd
import matplotlib.pyplot as plt

from config import (
    ZIP_SUMMARY_PATH,
    MONTH_SUMMARY_PATH,
    DESCRIPTOR_SUMMARY_PATH,
    ZIP_CHART_PATH,
    MONTH_CHART_PATH,
    DESCRIPTOR_CHART_PATH,
)

def summarize_by_zip(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("incident_zip", dropna=False)
        .agg(
            complaint_count=("unique_key", "count"),
            open_count=("status", lambda s: (s != "Closed").sum()),
            missing_location_count=("missing_location_flag", "sum"),
            median_days_to_close=("days_to_close", "median"),
        )
        .reset_index()
        .sort_values("complaint_count", ascending=False)
    )


def summarize_by_month(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("year_month")
        .agg(complaint_count=("unique_key", "count"))
        .reset_index()
        .sort_values("year_month")
    )

def save_analysis_outputs(
    by_zip: pd.DataFrame,
    by_month: pd.DataFrame,
    by_descriptor: pd.DataFrame,
) -> None:
    ZIP_SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

    by_zip.to_csv(ZIP_SUMMARY_PATH, index=False)
    by_month.to_csv(MONTH_SUMMARY_PATH, index=False)
    by_descriptor.to_csv(DESCRIPTOR_SUMMARY_PATH, index=False)

    create_zip_chart(by_zip, ZIP_CHART_PATH)
    create_month_chart(by_month, MONTH_CHART_PATH)
    create_descriptor_chart(by_descriptor, DESCRIPTOR_CHART_PATH)

def summarize_by_descriptor(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("descriptor", dropna=False)
        .agg(complaint_count=("unique_key", "count"))
        .reset_index()
        .sort_values("complaint_count", ascending=False)
    )

def create_zip_chart(by_zip: pd.DataFrame, output_path) -> None:
    top_zip = by_zip.head(10).sort_values("complaint_count")

    plt.figure(figsize=(10, 6))
    plt.barh(top_zip["incident_zip"].astype(str), top_zip["complaint_count"])
    plt.title("Top Queens ZIP Codes by Flooding-Related 311 Complaints")
    plt.xlabel("Complaint Count")
    plt.ylabel("ZIP Code")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def create_month_chart(by_month: pd.DataFrame, output_path) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(by_month["year_month"], by_month["complaint_count"], marker="o")
    plt.title("Monthly Flooding-Related 311 Complaints in Queens")
    plt.xlabel("Month")
    plt.ylabel("Complaint Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()

def create_descriptor_chart(by_descriptor: pd.DataFrame, output_path) -> None:
    top_descriptors = by_descriptor.head(10).sort_values("complaint_count")

    plt.figure(figsize=(10, 6))
    plt.barh(
        top_descriptors["descriptor"].astype(str),
        top_descriptors["complaint_count"]
    )
    plt.title("Top Flooding-Related 311 Complaint Descriptors in Queens")
    plt.xlabel("Complaint Count")
    plt.ylabel("Complaint Descriptor")
    plt.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path)
    plt.close()


