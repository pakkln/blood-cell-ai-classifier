from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data/raw/bloodmnist.npz"

REQUIRED_ARRAY = {
    "train_images",
    "train_labels",
    "test_images",
    "test_labels",
    "val_images",
    "val_labels"
}

def validate_raw(path: Path):
    with np.load(path, allow_pickle=False) as dataset:
        missing = REQUIRED_ARRAY - set(dataset.files)

        if missing:
            raise ValueError(f"Missing arrays: {missing}")
        
        for split in ["train","val","test"]:
            images = dataset[f"{split}_images"]
            labels = dataset[f"{split}_labels"]

            if images.ndim != 4 or images.shape[1:] != (28,28,3):
                raise ValueError(f"Invalid {split} image shape: {images.shape}")
            
            if labels.ndim != 2 or labels.shape[1] != 1:
                raise ValueError(f"Invalid {split} labels shape: {labels.shape}")
            
            if images.dtype != np.uint8:
                raise ValueError(f"Invalid {split} images data type: {images.dtype}")
            
            if labels.dtype != np.uint8:
                raise ValueError(f"Invalid {split} labels data type: {labels.dtype}")
            
            if images.shape[0] != labels.shape[0]:
                raise ValueError(
                    f"{split}: image count {images.shape[0]} "
                    f"does not match label count {labels.shape[0]}"
                )
            
            if np.any((labels < 0) | (labels > 7)):
                raise ValueError(f"{split}: invalid class id detected")
            
            if images.shape[0]==0:
                raise ValueError(f"{split}: is empty")

        print("Array validation passed")


if __name__ == "__main__":
    validate_raw(RAW_PATH)