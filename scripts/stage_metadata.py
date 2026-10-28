from pathlib import Path
import pandas as pd
import numpy as np

from scripts.validate_raw import validate_raw

ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "data/raw/bloodmnist.npz"
STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

def build_metadata(path : Path):
    validate_raw(path)

    records = []

    with np.load(path, allow_pickle=False) as dataset:
        for split in ["train","val","test"]:
            labels = dataset[f"{split}_labels"].flatten()

            for index, class_id in enumerate(labels):
                #generate stable image id
                image_id = f"{split}_{index:06d}"

                #add dictionary with images id, split, source index, class_id
                records.append({
                    "image_id":image_id,
                    "split": split,
                    "source_index": index,
                    "class_id" : int(class_id)
                })

    #convert record into a pandas dataframe
    metadata = pd.DataFrame(records)

    return metadata

if __name__ == ("__main__"):

    temp_path = STAGED_PATH.with_name(STAGED_PATH.name + ".tmp")

    df = build_metadata(RAW_PATH)
    STAGED_PATH.parent.mkdir(parents=True,exist_ok = True)

    try:
        df.to_parquet(temp_path, engine="pyarrow",index=False)

        saved_df = pd.read_parquet(temp_path)

        assert len(saved_df) == len(df)
        assert saved_df.columns.tolist() == df.columns.tolist()
        assert saved_df["image_id"].is_unique
        assert saved_df.equals(df)

        temp_path.replace(STAGED_PATH)
    finally:
        temp_path.unlink(missing_ok=True)

    print("Saved rows:", len(saved_df))
    print("Schema:", saved_df.dtypes)
    print(df.head())
    print("Rows: ",len(df))
    print(df.dtypes)