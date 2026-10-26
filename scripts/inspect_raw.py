from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data/raw/bloodmnist.npz"

with np.load(RAW_PATH, allow_pickle = False) as dataset:
    print(dataset.files)
    
    for name in dataset.files:
        array = dataset[name]
        print("Name: ",name)
        print("Shape: ",array.shape)
        print("Data Type: ",array.dtype)
        print() #new line
