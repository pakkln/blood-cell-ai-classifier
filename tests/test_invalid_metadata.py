from pathlib import Path
import sys
import tempfile
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

from scripts.check_metadata_quality import validate_metadata

STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

df = pd.read_parquet(STAGED_PATH)

#change class id of the first row to 99
df.loc[0, "class_id"] = 99

with tempfile.TemporaryDirectory() as tmpdir:
    test_path = Path(tmpdir) / "invalid_metadata.parquet"
    df.to_parquet(test_path, index = False)

    try:
        validate_metadata(test_path)

    except ValueError as error:
        assert "Invalid metadata records" in str(error)
        print("Pass: Invalid class id rejected")

    else:
        raise AssertionError("Fail: Invalid class id was accepted")