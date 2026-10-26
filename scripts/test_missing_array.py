#this file create random dataset for testing validate raw 
from pathlib import Path
import tempfile
import numpy as np

from validate_raw import validate_raw

with tempfile.TemporaryDirectory() as temp_dir:
    test_path = Path(temp_dir) / "invalid.npz"

    #create a small dataset with one missing array
    np.savez(
        test_path,
        train_images=np.zeros((2, 28, 28, 3), dtype=np.uint8),
        train_labels=np.array([[3], [9]], dtype=np.uint8),
        val_images=np.zeros((1, 28, 28, 3), dtype=np.uint8),
        val_labels=np.zeros((1, 1), dtype=np.uint8),
        test_images=np.zeros((1, 28, 28, 3), dtype=np.uint8),
        test_labels=np.zeros((1, 1), dtype=np.uint8),
    )

    try: validate_raw(test_path)
    except ValueError as error:
        print("Expected error: ",error)
    else:
        raise AssertionError("Invalide dataset was accepted")

