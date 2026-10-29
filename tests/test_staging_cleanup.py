from pathlib import Path
import tempfile
import pytest

def test_staging_cleanup():

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_path = Path(tmpdir) / "metadata.parquet.tmp"
        final_path = Path(tmpdir) / "metadata.parquet"

        #simulate an existing valide output
        final_path.write_text("original_data")

        try:
            with pytest.raises(RuntimeError, match="Simulated write failure"):
                try:
                    #simulate pipeline failure
                    raise RuntimeError("Simulated write failure")

                finally:
                    temp_path.unlink(missing_ok=True)

            assert not temp_path.exists()
            assert final_path.read_text() == "original_data"
        finally:
            temp_path.unlink(missing_ok=True)