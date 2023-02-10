from dataclasses import dataclass
import os
from resume_keyword.constants import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR) 
        self.TRAIN_ZIP_DATA_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, S3_TRAIN_DATA_FILE_NAME)
        self.TEST_ZIP_DATA_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, S3_TEST_DATA_FILE_NAME)
        self.UNZIP_TRAIN_FOLDER_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.UNZIP_TEST_FOLDER_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)


@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRAIN_TXT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TRAIN_TXT_FILE_NAME)
        self.TEST_TXT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TEST_TXT_FILE_NAME)


@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.MODEL_TRAINER_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR)
        self.TRAIN_ANNOTAIONS_PATH: str = os.path.join(from_root(), TRAIN_ANNOTATION_FILE_NAME)
        self.TEST_ANNOTAIONS_PATH: str = os.path.join(from_root(), TEST_ANNOTATION_FILE_NAME)
