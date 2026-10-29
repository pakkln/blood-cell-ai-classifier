from pathlib import Path
import tempfile
import pandas as pd
import pytest

from scripts.check_metadata_quality import validate_metadata

ROOT = Path(__file__).resolve().parents[1]
STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

def test_duplicate_metadata():
    df = pd.read_parquet(STAGED_PATH)

    #duplicate first record
    duplicate = df.iloc[[0]]

    #append dup row to original dataframe
    test_df = pd.concat([df,duplicate],ignore_index=True)
    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "duplicates.parquet"
        test_df.to_parquet(test_path, index=False)

        with pytest.raises(ValueError, match = "Duplicate metadata detected"):
            validate_metadata(test_path)


