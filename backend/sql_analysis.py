import duckdb
import pandas as pd


def execute_sql(
    df: pd.DataFrame,
    query: str,
    table_name: str = "dataset",
) -> pd.DataFrame:
    """
    Execute a read-only SQL query against a Pandas DataFrame.

    The DataFrame is exposed to DuckDB using the supplied table name.

    Args:
        df: Dataset to query.
        query: SQL SELECT query.
        table_name: Name used to reference the DataFrame in SQL.

    Returns:
        Query result as a Pandas DataFrame.

    Raises:
        ValueError: If the query is empty or is not a SELECT query.
        RuntimeError: If DuckDB cannot execute the query.
    """
    if not query.strip():
        raise ValueError("SQL query cannot be empty.")

    normalized_query = query.strip().lower()

    if not normalized_query.startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    connection = duckdb.connect(database=":memory:")

    try:
        connection.register(table_name, df)
        result = connection.execute(query).fetchdf()
        return result

    except duckdb.Error as exc:
        raise RuntimeError(f"SQL execution failed: {exc}") from exc

    finally:
        connection.close()