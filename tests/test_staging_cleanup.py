from pathlib import Path
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    temp_path = Path(tmpdir) / "metadata.parquet.tmp"
    final_path = Path(tmpdir) / "metadata.parquet"

    #simulate an existing valide output
    final_path.write_text("original_data")

    try:
        try:
            temp_path.write_text("incomplete data")

            #simulate pipeline failure
            raise RuntimeError("Simulated write failure")

        finally:
            temp_path.unlink(missing_ok=True)
    except RuntimeError as error:
        assert str(error) == "Simulated write failure"

    assert not temp_path.exists()
    assert final_path.read_text() == "original_data"

    print("PASS: temporary file cleaned up")
    print("Pass: original output preserved")