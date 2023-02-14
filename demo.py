
# 'mongodb+srv://iNeuron:RsPGmJUa69n558n@ineuron-ai-projects.7eh1w4s.mongodb.net/test'

from resume_keyword.components.data_ingestion import DataIngestion
from resume_keyword.components.data_transformation import DataTransformation
from resume_keyword.components.model_trainer import ModelTrainer
from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
from resume_keyword.configuration.s3_operations import S3Operation



data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(), S3_operations=S3Operation())

data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts, s3_opearations=S3Operation())

data_transformation_artifacts = data_transformation.initiate_data_transformation()

model_trainer = ModelTrainer(model_trainer_config=ModelTrainerConfig(), data_transformation_artifacts=DataIngestionArtifacts)

model_trainer.initiate_model_trainer()






