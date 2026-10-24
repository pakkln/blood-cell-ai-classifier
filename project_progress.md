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

Next milestone: Design a reproducible BloodMNIST ingestion pipeline using the existing repository and trained classifier.

Planned components: data validation, Parquet, DuckDB, ETL, batch inference, testing, and CI.