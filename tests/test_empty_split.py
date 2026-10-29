from pathlib import Path
import tempfile
import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[1]

from scripts.validate_raw import validate_raw

RAW_PATH = ROOT / "data/raw/bloodmnist.npz"

def test_empty_split():
    with np.load(RAW_PATH, allow_pickle = False) as dataset:
        arrays = {key: dataset[key] for key in dataset.files}

    arrays["val_images"] = np.empty((0,28,28,3), dtype = np.uint8)

    arrays["val_labels"] = np.empty((0,1), dtype = np.uint8)

    with tempfile.TemporaryDirectory() as tmpdir:
        test_path = Path(tmpdir) / "emptysplit.npz"
        np.savez(test_path, **arrays)

        with pytest.raises(ValueError, match="val: is empty"):
            validate_raw(test_path)