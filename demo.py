# from resume_keyword.components.data_ingestion import Data_ingestion
# from resume_keyword.components.data_transformation import DataTransformation
# from resume_keyword.components.model_trainer import ModelTrainer
# from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
# from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
from resume_keyword.configuration.s3_operations import S3Operation



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

def read_txt_file(filename: str) -> str:
        # Opening file for read only
    file1 = open(filename, "r", encoding='utf-8')
    # read all text
    text = file1.read()
    # close the file
    file1.close()
    
    return text




import os
import re
text = read_txt_file(filename="D:/txt/image_txt_0.txt")

# ***@***.com

def use_regex(input_text):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", re.IGNORECASE)
    return pattern.findall(input_text)


print(use_regex(text))
    
# email = re.findall(pattern='/[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+/g',string=text)


# print(email)
