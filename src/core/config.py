from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parents[2]

SOURCE_DOCUMENTS=(
    PROJECT_ROOT
    /"data"/"source_documents"
)

PROCESSED_DOCUMENTS=(
    PROJECT_ROOT
    /"data"/"processed_documents"
)