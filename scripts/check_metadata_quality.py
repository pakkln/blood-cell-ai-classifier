from pathlib import Path
import duckdb
from scripts.query_metadata import query_metadata


ROOT = Path(__file__).resolve().parents[1]
STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet"

def check_metadata_quality(path : Path):
    con = duckdb.connect(":memory:")
    query = """
        SELECT 
            image_id,
            split,
            source_index,
            class_id
        FROM read_parquet(?)
        WHERE
            image_id IS NULL
            OR class_id IS NULL
            OR class_id NOT BETWEEN 0 AND 7
            OR split NOT IN ('train','val','test')
            OR split IS NULL
            OR source_index IS NULL
            OR source_index < 0 
            OR image_id = '' --present but empty
    """

    result = con.execute(query, [str(path)]).fetchall()
    con.close()

    return result

def validate_metadata(path:Path):
    invalid_rows = check_metadata_quality(path)

    if(invalid_rows):
        raise ValueError(f"Invalid metadata records: {len(invalid_rows)}")
    

    duplicates = query_metadata(path)

    if(duplicates):
        raise ValueError(f"Duplicate metadata detected: {len(duplicates)}")
    
    print("Metadata validation passed")

if __name__ == "__main__":
    invalid_rows = check_metadata_quality(STAGED_PATH)
    print("Invalid records:", len(invalid_rows))
    validate_metadata(STAGED_PATH)
