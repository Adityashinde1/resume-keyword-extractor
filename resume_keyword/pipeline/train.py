import sys
from resume_keyword.components.data_ingestion import DataIngestion
from resume_keyword.components.data_transformation import DataTransformation
from resume_keyword.components.model_trainer import ModelTrainer
from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts, DataTransformationArtifacts, ModelTrainerArtifacts
from resume_keyword.configuration.s3_operations import S3Operation
from resume_keyword.exception import ResumeKeywordException
from resume_keyword.constants import *
import logging

# initializing logger
logger = logging.getLogger(__name__)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_transformation_config = DataTransformationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        self.s3_operations = S3Operation()


    # This method is used to start the data ingestion
    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logger.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logger.info("Getting the data from S3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config, S3_operations=self.s3_operations)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logger.info("Got the resume pdf from S3 bucket")
            logger.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    # This method is used to start the data validation
    def start_data_transformation(
        self, data_ingestion_artifact: DataIngestionArtifacts
    ) -> DataTransformationArtifacts:
        logger.info("Entered the start_data_transformation method of TrainPipeline class")
        try:
            data_transformation = DataTransformation(data_transformation_config=self.data_transformation_config, data_ingestion_artifacts=data_ingestion_artifact,
            s3_operations=self.s3_operations)

            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logger.info("Performed the data transformation operation")
            logger.info(
                "Exited the start_data_transformation method of TrainPipeline class"
            )
            return data_transformation_artifact

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    # This method is used to start the model trainer
    def start_model_trainer(
        self, data_transformation_artifact: DataTransformationArtifacts) -> ModelTrainerArtifacts:
        logger.info("Entered the start_model_trainer method of TrainPipeline class")
        try:
            model_trainer = ModelTrainer(
                data_transformation_artifacts=data_transformation_artifact,
                model_trainer_config=self.model_trainer_config
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()

            logger.info(
                "Exited the start_data_transformation method of TrainPipeline class"
            )
            return model_trainer_artifact

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    def run_pipeline(self) -> None:
        logger.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact) 

            logger.info(
                "Exited the run_pipeline method of TrainPipeline class"
            )
            
        except Exception as e:
            raise ResumeKeywordException(e, sys) from e