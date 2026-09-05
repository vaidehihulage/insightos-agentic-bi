import pandas as pd


def profile_dataset(df: pd.DataFrame) -> dict:
    """
    Generate a basic profile of a Pandas DataFrame.

    Returns:
        A dictionary containing dataset-level and column-level statistics.
    """
    if df.empty:
        raise ValueError("Dataset is empty.")

    column_profiles = {}

    for column in df.columns:
        series = df[column]

        column_profiles[column] = {
            "dtype": str(series.dtype),
            "missing_count": int(series.isna().sum()),
            "missing_percentage": round(
                float(series.isna().mean() * 100), 2
            ),
            "unique_count": int(series.nunique(dropna=True)),
        }

    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns.tolist()

    numeric_summary = {}

    if numeric_columns:
        summary = df[numeric_columns].describe().to_dict()

        for column, stats in summary.items():
            numeric_summary[column] = {
                key: float(value)
                for key, value in stats.items()
            }

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "column_profiles": column_profiles,
        "numeric_summary": numeric_summary,
    }