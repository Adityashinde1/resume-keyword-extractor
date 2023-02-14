import os
from os import environ
from datetime import datetime
from from_root import from_root

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join(from_root(), "artifacts", TIMESTAMP)
LOGS_DIR = "logs"
LOGS_FILE_NAME = "resume_keyword.log"


BUCKET_NAME = "resume-keyword-extractor"


DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
S3_TRAIN_DATA_FILE_NAME = "resume_data_train.zip"
S3_TEST_DATA_FILE_NAME = "resume_data_test.zip"
UNZIP_TRAIN_DATA_FOLDER_NAME = "resume_data_train"
UNZIP_TEST_DATA_FOLDER_NAME = "resume_data_test"


DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
TRAIN_PDF_IMAGES_FOLDER_NAME = "train_resume_pdf_images"
TEST_PDF_IMAGES_FOLDER_NAME = "test_resume_pdf_images"
TRAIN_RESUME_TXT_FILE_FOLDER_NAME = "train_resume_txt_files"
TEST_RESUME_TXT_FILE_FOLDER_NAME = "test_resume_txt_files"
TRAIN_TXT_FILE_NAME = "train_result.txt"
TEST_TXT_FILE_NAME = "test_result.txt"

MODEL_TRAINER_ARTIFACTS_DIR = "ModelTrainerArtifacts"
BEST_MODEL_FOLDER_NAME = "model-best"
TRAIN_ANNOTATION_FILE_NAME = "train_annotations.json"
TEST_ANNOTATION_FILE_NAME = "test_annotations.json"
SPACY_TRAIN_DATA_FORMAT_NAME = "training_data.spacy"
SPACY_TEST_DATA_FORMAT_NAME = "testing_data.spacy"
CONFIG_FILE_NAME = "config.cfg"

MODEL_PREDICTOR_ARTIFACTS_DIR = 'ModelPredictorArtifacts'
PDF_TO_IMG_DIR = 'pdf_to_img'
IMG_TO_TXT_DIR = 'img_to_txt'
MONGO_URL = environ['MONGO_URL']
DB_NAME = "ineuron"
COLLECTION_NAME = "resume-keyword"

APP_HOST = "0.0.0.0"
PORT = 8000