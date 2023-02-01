from resume_keyword.components.data_ingestion import Data_ingestion
from resume_keyword.components.data_transformation import DataTransformation
from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
from resume_keyword.configuration.s3_operations import S3Operation



data_ingestion = Data_ingestion(data_ingestion_config=DataIngestionConfig(), S3_operations=S3Operation())

data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts, s3_opearations=S3Operation())

data_transformation.initiate_data_transformation()

