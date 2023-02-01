from dataclasses import dataclass
import os
from resume_keyword.utils.main_utils import MainUtils
from resume_keyword.constants import *


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR) 
        self.ZIP_DATA_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, S3_DATA_FOLDER_NAME)
        self.UNZIP_FOLDER_PATH: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)


@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.UTILS = MainUtils()
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TXT_FILE_PATH: str = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR, TXT_FILE_NAME)
