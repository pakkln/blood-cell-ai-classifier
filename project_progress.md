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

### Remaining Phase 1 Tasks
- Review and clean the training notebook
- Finalize README and dataset attribution
- Verify reproducibility documentation

## Phase 2: Data Engineering

### M1 — Task 1: Raw Dataset Ingestion

Status: Completed — October 26, 2026

**Implemented**
- Created `scripts/ingest_raw.py`.
- Downloaded official BloodMNIST data from Zenodo.
- Stored the original dataset in `data/raw/bloodmnist.npz`.
- Implemented checksum verification using MD5.
- Implemented temporary-file download and cleanup on failure.
- Added existing-file detection to avoid unnecessary downloads.
- Confirmed that the raw dataset is excluded from Git.

**Verified**
- Initial download completed successfully.
- Second execution returned `Already downloaded`.
- Local dataset MD5 matched the expected checksum.
- Source code review passed.
- Failure-handling branches have been reviewed but not independently tested.

**Next task:** M1 — Task 2: Inspect the raw BloodMNIST dataset structure and establish its schema.

Planned components: data validation, Parquet, DuckDB, ETL, batch inference, testing, and CI.