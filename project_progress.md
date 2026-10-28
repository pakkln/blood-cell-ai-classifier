# Project Progress — BloodMNIST ML Platform

## Phase 1: ML Classifier

Status: Core implementation complete; final documentation and notebook cleanup pending.

### Dataset and Model
- Dataset: Official BloodMNIST (MedMNIST)
- Framework: PyTorch
- Input: 3 × 28 × 28 RGB images
- Architecture: Two Conv2d blocks with ReLU and MaxPooling, followed by a linear classifier
- Optimizer: Adam, learning rate 0.001
- Loss: CrossEntropyLoss
- Preprocessing: ToTensor

### Final Results
| Metric | Validation | Test |
|---|---:|---:|
| Accuracy | 90.36% | 89.48% |
| Loss | 0.2852 | 0.3087 |
| Macro F1 | 0.8904 | 0.8804 |

Selected checkpoint: `models/bloodmnist_cnn_10epochs.pth`

Checkpoint SHA256: `8884f42fa148ab57a5ed9d11c15cbf6998c1394171048708041d737211a74f6d`

### Verified Engineering Work
- Implemented CNN training and validation loops
- Evaluated per-class precision, recall, F1, and confusion matrices
- Selected checkpoint using validation loss
- Completed final held-out test evaluation
- Exported evaluation metrics to JSON
- Created reusable model and inference modules
- Verified standalone inference on Google Colab and macOS
- Committed and pushed Phase 1 source files to GitHub

### Known Limitations
- Frequent confusion between classes 3 and 5
- Training-run continuity was not fully established
- External clinical generalization has not been evaluated
- Not intended for medical diagnosis



## Phase 2: Data Engineering


### Phase 2 — Day 2 (October 27, 2026)

**Status:** Core metadata staging milestone completed.

**Verified accomplishments:**
- Extended `validate_raw.py` to reject empty dataset splits.
- Created and passed `tests/test_empty_split.py`.
- Created `scripts/stage_metadata.py`.
- Extracted 17,092 metadata records from the official BloodMNIST train, validation, and test splits.
- Generated stable image IDs using split names and zero-padded source indices.
- Created Parquet metadata with four columns: `image_id`, `split`, `source_index`, and `class_id`.
- Verified Parquet row count, column names, unique image IDs, and DataFrame equality after reading the file.
- Implemented temporary-file writing and atomic replacement of the final Parquet file.
- Successfully executed the staging pipeline twice.
- Confirmed the final 198 KB Parquet file exists without a remaining temporary file.
- Confirmed generated Parquet data does not appear in Git status.

**Current output:** `data/staged/bloodmnist_metadata.parquet`

**Known limitation:** Temporary-file cleanup on failure and concurrent-writer protection are not yet implemented.

### Phase 2 — Day 3 (October 28, 2026)

**Status:** Metadata quality and pipeline reliability milestone verified.

**Completed:**
- Implemented SQL metadata quality checks using DuckDB.
- Added checks for invalid class IDs, invalid split names, and missing metadata values.
- Created reusable `validate_metadata()` to check invalid records and duplicate image IDs.
- Verified duplicate detection using SQL `GROUP BY` and `HAVING`.
- Added negative regression tests using temporary corrupted Parquet datasets.
- Verified rejection of invalid class IDs and duplicate image IDs.
- Implemented `try/finally` cleanup in the Parquet staging script.
- Verified temporary-file cleanup and preservation of existing output using a simulated failure.
- Successfully regenerated 17,092 Parquet metadata records.
- Ran all six verification commands successfully.

**Files modified or created:**
- `scripts/stage_metadata.py`
- `scripts/check_metadata_quality.py`
- `scripts/query_metadata.py`
- `tests/test_duplicate_metadata.py`
- `tests/test_invalid_metadata.py`
- `tests/test_staging_cleanup.py`

**Known limitations:**
- Cleanup failure test is a simulation, not an integration test of the actual staging script.
- Parquet schema and relationships between metadata fields are not yet fully enforced.
- Automated pytest tests and GitHub Actions CI are not yet configured.
- Concurrent staging processes are not supported.

**Next milestone:** Introduce pytest and automate the existing data-quality tests before extending the pipeline.


Planned components: data validation, Parquet, DuckDB, ETL, batch inference, testing, and CI.