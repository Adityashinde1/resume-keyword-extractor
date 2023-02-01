import os
from datetime import datetime
from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join(from_root(), "artifacts", TIMESTAMP)
LOGS_DIR = 'logs' 
LOGS_FILE_NAME = 'resume_keyword.log'


BUCKET_NAME = 'reusme-keyword-extractor'
S3_DATA_FOLDER_NAME = "resume_data.zip"
PDF_IMAGES_FOLDER_NAME = 'resume_pdf_images'
UNZIP_FOLDER_NAME = 'resume_data'
RESUME_TXT_FILE_FOLDER_NAME = 'resume_txt_files'

DATA_INGESTION_ARTIFACTS_DIR = 'DataIngestionArtifacts'

POPPLER_PATH = 'C:/Program Files/poppler-0.68.0/bin'
TESSERACT_CMD = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
DATA_TRANSFORMATION_ARTIFACTS_DIR = 'DataTransformationArtifacts'
TXT_FILE_NAME = 'result.txt'