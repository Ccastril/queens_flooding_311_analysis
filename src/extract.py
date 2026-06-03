import pandas as pd
from sodapy import Socrata

from config import DATASET_ID, DOMAIN, QUERY_LIMIT, RAW_DATA_PATH, QUERY_SQL_PATH

def load_query(limit: int = QUERY_LIMIT) -> str:
    query_template = QUERY_SQL_PATH.read_text(encoding="utf-8")
    return query_template.format(limit=limit)

def fetch_queens_flooding_records(limit: int = QUERY_LIMIT) -> pd.DataFrame:
    client = Socrata(DOMAIN, None)
    query = load_query(limit)

    results = client.get(DATASET_ID, query=query)
    return pd.DataFrame.from_records(results)

def save_raw_data(df: pd.DataFrame) -> None:
    df.to_csv(RAW_DATA_PATH, index=False)