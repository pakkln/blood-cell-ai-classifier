from pathlib import Path
import sys
import tempfile
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from scripts.validate_raw import validate_raw

RAW_PATH = ROOT / "data/raw/bloodmnist.npz"

with np.load(RAW_PATH, allow_pickle = False) as dataset:
    arrays = {key: dataset[key] for key in dataset.files}

arrays["val_images"] = np.empty((0,28,28,3), dtype = np.uint8)

arrays["val_labels"] = np.empty((0,1), dtype = np.uint8)

with tempfile.TemporaryDirectory() as tmpdir:
    test_path = Path(tmpdir) / "emptysplit.npz"
    np.savez(test_path, **arrays)

    try:
        validate_raw(test_path)
    except ValueError as error:
        assert "val: is empty" in str(error)
        print("PASS: Empty split rejected")

    else: 
        raise AssertionError("Fail: Empty split was accepted")