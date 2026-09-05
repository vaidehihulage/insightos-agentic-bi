import pandas as pd
import pytest

from backend.data_ingestion import get_dataset_metadata, load_csv


def test_load_csv():
    df = load_csv("data/sample/sales_sample.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5


def test_dataset_metadata():
    df = load_csv("data/sample/sales_sample.csv")

    metadata = get_dataset_metadata(df)

    assert metadata["rows"] == 5
    assert metadata["columns"] == 4
    assert metadata["column_names"] == [
        "order_id",
        "product",
        "region",
        "revenue",
    ]


def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        load_csv("data/sample/does_not_exist.csv")


def test_reject_non_csv_file():
    with pytest.raises(ValueError):
        load_csv("README.md")