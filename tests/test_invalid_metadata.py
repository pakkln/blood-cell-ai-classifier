from pathlib import Path
import sys
import tempfile
import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]


STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

from scripts.check_metadata_quality import validate_metadata


def test_invalid_class_id():
    df = pd.read_parquet(STAGED_PATH)

    df.loc[0,"class_id"]=99

    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "invalid_metadata.parquet"
        df.to_parquet(test_path, index = False)

        with pytest.raises(ValueError, match = "Invalid metadata records"):
            validate_metadata(test_path)

