import pandas as pd
import pytest

from backend.sql_analysis import execute_sql


@pytest.fixture
def sales_df():
    return pd.DataFrame(
        {
            "product": [
                "Laptop",
                "Mouse",
                "Keyboard",
                "Monitor",
                "Headphones",
            ],
            "region": [
                "West",
                "North",
                "South",
                "West",
                "East",
            ],
            "revenue": [
                75000,
                1500,
                3000,
                18000,
                4500,
            ],
        }
    )


def test_select_all(sales_df):
    result = execute_sql(
        sales_df,
        "SELECT * FROM dataset",
    )

    assert len(result) == 5


def test_revenue_aggregation(sales_df):
    result = execute_sql(
        sales_df,
        "SELECT SUM(revenue) AS total_revenue FROM dataset",
    )

    assert result.iloc[0]["total_revenue"] == 102000


def test_group_by_region(sales_df):
    result = execute_sql(
        sales_df,
        """
        SELECT region, SUM(revenue) AS total_revenue
        FROM dataset
        GROUP BY region
        ORDER BY total_revenue DESC
        """,
    )

    assert result.iloc[0]["region"] == "West"
    assert result.iloc[0]["total_revenue"] == 93000


def test_filtering(sales_df):
    result = execute_sql(
        sales_df,
        """
        SELECT product, revenue
        FROM dataset
        WHERE revenue > 10000
        """,
    )

    assert len(result) == 2


def test_reject_non_select_query(sales_df):
    with pytest.raises(ValueError):
        execute_sql(
            sales_df,
            "DELETE FROM dataset",
        )


def test_empty_query(sales_df):
    with pytest.raises(ValueError):
        execute_sql(sales_df, "")


def test_invalid_sql(sales_df):
    with pytest.raises(RuntimeError):
        execute_sql(
            sales_df,
            "SELECT unknown_column FROM dataset",
        )