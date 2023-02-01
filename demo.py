from resume_keyword.components.data_ingestion import Data_ingestion
from resume_keyword.entity.config_entity import DataIngestionConfig
from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
from resume_keyword.configuration.s3_operations import S3Operation


data_ingestion = Data_ingestion(data_ingestion_config=DataIngestionConfig(), S3_operations=S3Operation())

data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()