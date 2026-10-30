import torch
import json
from pathlib import Path
from model import create_cnn

import numpy as np
import pandas as pd
from PIL import Image
from torchvision.transforms import ToTensor


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "model_config.json"

RAW_PATH = ROOT / "data/raw/bloodmnist.npz"
STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

def load_model():
    #load existing config
    with CONFIG_PATH.open("r") as file:
        config = json.load(file)

    model = create_cnn()
    checkpoint_path = ROOT / config["checkpoint"]

    state_dict = torch.load(
        checkpoint_path,
        map_location = "cpu",
        weights_only = True
    )

    model.load_state_dict(state_dict)

    model.eval()

    return model, config

def load_sample_image(raw_path: Path, metadata_row):
    split = metadata_row["split"]
    index = int (metadata_row["source_index"])

    with np.load(raw_path, allow_pickle=False) as dataset:
        #find correct image array
        image_array = dataset[f"{split}_images"][index]

    image = Image.fromarray()

    image_tensor = image.ToTensor()

    return image_tensor

if __name__ == "__main__":
    model, config = load_model()
    metadata = pd.read_parquet(STAGED_PATH)
    sample = metadata.iloc[0]

    image_tensor = load_sample_image(RAW_PATH, sample)

    print("Image ID:", sample["image_id"])
    print("Image tensor shape:", image_tensor.shape)
    print("Tensor dtype:", image_tensor.dtype)
    print("Min pixel:", image_tensor.min().item())
    print("Max pixel:", image_tensor.max().item())
