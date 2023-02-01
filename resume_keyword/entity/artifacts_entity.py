from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifacts:
    pdf_zip_file_path: str
    pdf_folder_path: str


# Data Transformation Artifacts
@dataclass
class DataTransformationArtifacts:
    resume_pdf_images_path: str
    resume_txt_files_path: str
    txt_filepath: str