from pathlib import Path

import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        Loaded Pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the supplied file is not a CSV.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are currently supported.")

    return pd.read_csv(path)


def get_dataset_metadata(df: pd.DataFrame) -> dict:
    """
    Return basic metadata about a dataset.
    """
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
    }