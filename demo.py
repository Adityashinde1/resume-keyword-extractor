# from resume_keyword.components.data_ingestion import Data_ingestion
# from resume_keyword.components.data_transformation import DataTransformation
# from resume_keyword.components.model_trainer import ModelTrainer
# from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
# from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
# from resume_keyword.configuration.s3_operations import S3Operation



# data_ingestion = Data_ingestion(data_ingestion_config=DataIngestionConfig(), S3_operations=S3Operation())

# data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

# data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts, s3_opearations=S3Operation())

# data_transformation_artifacts = data_transformation.initiate_data_transformation()

# model_trainer = ModelTrainer(model_trainer_config=ModelTrainerConfig(), data_transformation_artifacts=DataIngestionArtifacts)

# model_trainer.initiate_model_trainer()


# from resume_keyword.entity.config_entity import DataIngestionConfig

# config = DataIngestionConfig()
# print(config.UNZIP_TRAIN_FOLDER_PATH)

# import spacy

# import warnings

# warnings.filterwarnings("ignore")

# nlp_ner = spacy.load("model-best")

# doc = nlp_ner("python,C++,Java,Aditya")

# for skill in doc.ents:
#     print(skill)

# import os

# path = 'D:/ineuron_org/dl_proj/resume-keyword-extractor/annotations'
# comd = f'aws s3 sync s3://resume-keyword-extractor/annotations/{path}'

# os.system(comd)



from resume_keyword.pipeline.train_pipeline import TrainPipeline

tp = TrainPipeline()

tp.run_pipeline()