from pathlib import Path
import duckdb

ROOT = Path(__file__).resolve().parents[1] 
#find project's root directory
#root = [convert path of current python script to path object].gets it absolute. /Users/phak/bloodcell-ml-platform
# parents[0] = /Users/phak/bloodcell-ml-platform/scripts, [1]=/Users/phak/bloodcell-ml-platform
#root = /Users/phak/bloodcell-ml-platform
STAGED_PATH = ROOT / "data/staged/bloodmnist_metadata.parquet" #tell location where the staged_path be,what does root mean

def query_metadata(path:Path):

    #connect to an in memory duck db database
    con = duckdb.connect(":memory:")

    #counts image
    query = """
        SELECT
            split,
            class_id,
            COUNT(*) AS image_count
        FROM read_parquet(?)
        GROUP BY split, class_id
        ORDER BY split, class_id
        """
    
    query2 = """
        SELECT 
            image_id,
            count(*) as occurence
        FROM read_parquet(?)
        GROUP BY image_id
        HAVING COUNT(*)>1
    """
    
    result = con.execute(query2, [str(path)]).fetchall() 

    con.close()

    return result

if __name__ == "__main__": 
    result = query_metadata(STAGED_PATH)
    for row in result:
        print(row)
        print("Duplicate IDs:", result)