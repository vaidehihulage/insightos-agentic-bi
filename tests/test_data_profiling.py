import pandas as pd
import pytest

from backend.data_profiling import profile_dataset


def test_profile_dataset_basic():
    df = pd.DataFrame(
        {
            "product": ["Laptop", "Mouse", "Laptop"],
            "revenue": [75000, 1500, 75000],
        }
    )

    profile = profile_dataset(df)

    assert profile["rows"] == 3
    assert profile["columns"] == 2
    assert "revenue" in profile["numeric_columns"]
    assert "product" in profile["categorical_columns"]


def test_missing_values():
    df = pd.DataFrame(
        {
            "product": ["Laptop", None, "Mouse"],
            "revenue": [75000, 1500, None],
        }
    )

    profile = profile_dataset(df)

    assert profile["column_profiles"]["product"]["missing_count"] == 1
    assert profile["column_profiles"]["revenue"]["missing_count"] == 1


def test_duplicate_rows():
    df = pd.DataFrame(
        {
            "product": ["Laptop", "Laptop"],
            "revenue": [75000, 75000],
        }
    )

    profile = profile_dataset(df)

    assert profile["duplicate_rows"] == 1


def test_numeric_summary():
    df = pd.DataFrame(
        {
            "revenue": [100, 200, 300]
        }
    )

    profile = profile_dataset(df)

    assert profile["numeric_summary"]["revenue"]["mean"] == 200.0


def test_empty_dataset():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        profile_dataset(df)