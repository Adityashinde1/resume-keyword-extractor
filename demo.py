
# 'mongodb+srv://iNeuron:RsPGmJUa69n558n@ineuron-ai-projects.7eh1w4s.mongodb.net/test'

# from resume_keyword.components.data_ingestion import DataIngestion
# from resume_keyword.components.data_transformation import DataTransformation
# from resume_keyword.components.model_trainer import ModelTrainer
# from resume_keyword.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig
# from resume_keyword.entity.artifacts_entity import DataIngestionArtifacts
# from resume_keyword.configuration.s3_operations import S3Operation



# data_ingestion = DataIngestion(data_ingestion_config=DataIngestionConfig(), S3_operations=S3Operation())

# data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()

# data_transformation = DataTransformation(data_transformation_config=DataTransformationConfig(), data_ingestion_artifacts=data_ingestion_artifacts, s3_opearations=S3Operation())

# data_transformation_artifacts = data_transformation.initiate_data_transformation()

# model_trainer = ModelTrainer(model_trainer_config=ModelTrainerConfig(), data_transformation_artifacts=DataIngestionArtifacts)

# model_trainer.initiate_model_trainer()

import re

def use_regex(input_text: str):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")
    #pattern = re.compile(r"^\S+@\S+\.\S+$")

    k = pattern.findall(input_text)
    return k

def email(inpute_text):
    pattern = r'^\S+@\S+\.\S+$'
    return re.findall(pattern, inpute_text)

text = '''Hi my name is aditya shinde. My email id is shindeadi39@gmail.com. klhjiusd jbfjhbih jgfyf v bfmnbfo; uhbfubfkljb 
ifhnhdfgehfm i9hfbfiju fh kjvbyuh yugfyueg fyoqgfiuyg fyug fyuwqgf8qegfyg yugfyuoweg fywg fgfyu wg fyuoweg fyuwg fyuoweg fiyegfyuowg fugfy8o7weg fiwygf6yg fiuwg f87g fiuf 
biuwhf9u8qhyfuhqf fiu phyfu87h f87 fuqhf87 ugfiuwgfjhyuhfjkshdfoi uhgbjhyugf ghiugfjkiuhg fuiphg gfg uhgfyugfyhg iu wuefha;h fahf ygf iuwahfiug fhiuhgf ,mnsdbvjkvbb jigvjsdbv
klhvjbv jb vbyuhgvjbv hgbvhgv hgvbgb v iuhghbd bjhlghgbyu guoig fuGFGF IPUGHF GBJKHBD HI UHIUHIU    hiuh fiuuh iu uhviuhbjkhbu jkahiu agvvu;ah  uhiug vb jhubvjk hgyug'''


g = use_regex(text)
print(g)