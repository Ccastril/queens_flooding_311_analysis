from extract import fetch_queens_flooding_records, save_raw_data
from transform import clean_flooding_records, save_cleaned_data
from analyze import summarize_by_zip, summarize_by_month, save_analysis_outputs, summarize_by_descriptor
from validate import create_validation_summary, save_validation_summary
from report import create_summary_report, save_summary_report


def main() -> None:
    print("Fetching raw data...")
    raw_df = fetch_queens_flooding_records()
    print(f"Fetched {len(raw_df)} rows.")

    print("Saving raw data...")
    save_raw_data(raw_df)

    print("Cleaning data...")
    cleaned_df = clean_flooding_records(raw_df)
    print(f"Cleaned {len(cleaned_df)} rows.")
    print("Saving cleaned data...")
    save_cleaned_data(cleaned_df)

    print("Creating validation summary...")
    validation_summary = create_validation_summary(cleaned_df)
    print("Saving validation summary...")
    save_validation_summary(validation_summary)

    by_zip = summarize_by_zip(cleaned_df)
    by_month = summarize_by_month(cleaned_df)
    by_descriptor = summarize_by_descriptor(cleaned_df)

    save_analysis_outputs(by_zip, by_month, by_descriptor)
    print("Creating written summary...")
    
    summary_report = create_summary_report(
        cleaned_df,
        by_zip,
        by_month,
        by_descriptor,
        validation_summary,
    )
    save_summary_report(summary_report)
    print("Done.")


if __name__ == "__main__":
    main()