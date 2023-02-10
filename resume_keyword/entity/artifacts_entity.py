from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifacts:
    train_pdf_file_path: str
    test_pdf_file_path: str


# Data Transformation Artifacts
@dataclass
class DataTransformationArtifacts:
    train_resume_pdf_images_path: str
    test_resume_pdf_images_path: str
    train_resume_txt_files_path: str
    test_resume_txt_files_path: str


# Model Trainer Artifacts
@dataclass
class ModelTrainerArtifacts:
    best_model_path: str