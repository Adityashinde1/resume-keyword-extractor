import os
import sys
import logging
from zipfile import ZipFile, Path
from resume_keyword.constants import *
from resume_keyword.exception import ResumeKeywordException
from resume_keyword.entity.config_entity import DataIngestionConfig
from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
from resume_keyword.configuration.s3_operations import S3Operation

logger = logging.getLogger(__name__)


class Data_ingestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig, S3_operations: S3Operation) -> None:
        self.data_ingestion_config = data_ingestion_config
        self.S3_operations = S3_operations


    def get_pdf_from_s3(self, bucket_file_name: str, bucket_name: str, output_filepath: str) -> zip:
        logger.info("Entered the get_data_from_s3 method of Data ingestion class")
        try:
            self.S3_operations.read_data_from_s3(bucket_file_name, bucket_name, output_filepath)

            logger.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e 


    def unzip_file(self, zip_data_filepath: str, unzip_dir_path: str) -> Path:
        logger.info("Entered the unzip_file method of Data ingestion class")
        try:
            with ZipFile(zip_data_filepath, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir_path)
            logger.info("Exited the unzip_file method of Data ingestion class")
            return unzip_dir_path

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e 
        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        try:
            logger.info("Entered the initiate_data_ingestion method of Data ingestion class")

            # Creating Data Ingestion Artifacts directory inside artifact folder
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)
            logger.info(
                f"Created {os.path.basename(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)} directory."
            )
            
            self.get_pdf_from_s3(bucket_file_name=S3_DATA_FOLDER_NAME, bucket_name=BUCKET_NAME,
                                               output_filepath=self.data_ingestion_config.ZIP_DATA_PATH)
            logger.info("Downloaded images zip file from S3 bucket")

            # Unzipping the file
            self.unzip_file(zip_data_filepath=self.data_ingestion_config.ZIP_DATA_PATH, unzip_dir_path=self.data_ingestion_config.UNZIP_FOLDER_PATH)
            logger.info("Extracted the images from the zip file")

            # Saving data ingestion artifacts
            data_ingestion_artifacts = DataIngestionArtifacts(pdf_zip_file_path=self.data_ingestion_config.UNZIP_FOLDER_PATH,
                                                              pdf_folder_path=os.path.join(self.data_ingestion_config.UNZIP_FOLDER_PATH, UNZIP_FOLDER_NAME)) 

            logger.info("Exited the initiate_data_ingestion method of Data ingestion class")
            return data_ingestion_artifacts

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
 
