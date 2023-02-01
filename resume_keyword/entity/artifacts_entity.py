from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifacts:
    pdf_zip_file_path: str
    pdf_folder_path: str


# Data Transformation Artifacts
@dataclass
class DataTransformationArtifacts:
    pass