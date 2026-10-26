from pathlib import Path
from urllib.request import urlretrieve
import hashlib

ROOT = Path(__file__).resolve().parents[1]
#Find the repository root based on the script location

SOURCE_URL = (
    "https://zenodo.org/records/10519652/"
    "files/bloodmnist.npz?download=1"
)

EXPECTED_MD5 = "7053d0359d879ad8a5505303e11de1dc"


#destination for original dataset 
RAW_PATH = ROOT / "data/raw/bloodmnist.npz"
#temporary file used during downloading
TEMP_PATH = RAW_PATH.with_suffix(".npz.part")


def calculate_md5(path: Path) -> str:
    digest = hashlib.md5()
    #create checksum for integrity verification

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            #read the file in 1 mb chuncks to avoid load everythings
            digest.update(chunk)

    return digest.hexdigest()

def ingest():
    RAW_PATH.parent.mkdir(parents = True, exist_ok = True)
    #RAW_PATH @ data/raw/bloodmnsit.npz
    # .parent = get data/raw, .mkdir = make directory
    # parents=True: create missing parent dir too, exist_ok = True: if directory exist, no return error

    #1 check whether the datset already exist
    if RAW_PATH.exists():
        if calculate_md5(RAW_PATH) == EXPECTED_MD5:
            print("Already downloaded")
            return
        else:
            raise ValueError("Existing file has an incorrect checksum")
            #raise = stops execution and reports an error
        
    try:
        urlretrieve(SOURCE_URL, TEMP_PATH)

        if calculate_md5(TEMP_PATH) != EXPECTED_MD5:
            raise ValueError("Downloaded file has an incorrect checksum")
        
        #4. move the verified file to its final location
        TEMP_PATH.replace(RAW_PATH)
    
    except Exception:
        TEMP_PATH.unlink(missing_ok=True)
        #deletes the temporary file if it exists
        raise

    print("Download completed")

if __name__ == "__main__":
    ingest()

#__name__ how the file is being executed
#__main__ = the files will run directly