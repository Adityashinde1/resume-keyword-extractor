import os
import sys
import logging
import spacy
import json
from spacy.tokens import DocBin
from resume_keyword.utils.main_utils import MainUtils
from resume_keyword.configuration.s3_operations import S3Operation
from tqdm import tqdm
from resume_keyword.constants import *
from resume_keyword.exception import ResumeKeywordException
from resume_keyword.entity.artifacts_entity import DataTransformationArtifacts, ModelTrainerArtifacts
from resume_keyword.entity.config_entity import ModelTrainerConfig

logger = logging.getLogger(__name__)


class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
        data_transformation_artifacts: DataTransformationArtifacts,
    ) -> None:
        self.model_trainer_config = model_trainer_config
        self.data_transformation_artifacts = data_transformation_artifacts
        self.utils = MainUtils()
        self.s3 = S3Operation()

    def get_annotations_from_s3(
        self, bucket_name: str, local_folder_path: str, bucket_folder_name: str
    ):
        try:
            logger.info(
                "Entered the get_annotations_from_s3 method of Model trainer class"
            )
            command: str = f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {local_folder_path} "

            os.system(command)
            logger.info(
                "Exited the get_annotations_from_s3 method of Model trainer class"
            )

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    def create_spacy_format_data(
        self, data: json, docbin_obj: object, output_file_path: str, nlp_model: object
    ):
        try:
            logger.info(
                "Entered the create_spacy_format_data method of Model trainer class"
            )
            for text, annot in tqdm(data["annotations"]):
                doc = nlp_model.make_doc(text)
                ents = []
                for start, end, label in annot["entities"]:
                    span = doc.char_span(
                        start, end, label=label, alignment_mode="contract"
                    )
                    if span is None:
                        print("Skipping entity")
                    else:
                        ents.append(span)
                doc.ents = ents
                docbin_obj.add(doc)

            docbin_obj.to_disk(output_file_path)  # save the docbin object
            logger.info(
                "Exited the create_spacy_format_data method of Model trainer class"
            )

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            logger.info(
                "Entered the initiate_model_trainer method of Model trainer class"
            )

            os.makedirs(
                self.model_trainer_config.MODEL_TRAINER_ARTIFACTS_DIR, exist_ok=True
            )
            logger.info(
                f"Created {os.path.basename(self.model_trainer_config.MODEL_TRAINER_ARTIFACTS_DIR)} directory."
            )

            # load a new spacy model
            nlp = spacy.blank("en")
            logger.info("Loaded new blank spacy model.")

            # create a DocBin object
            db = DocBin()
            logger.info("Created a new blank spacy model.")

            self.s3.download_file(
                bucket_name=BUCKET_NAME,
                output_file_path=self.model_trainer_config.TRAIN_ANNOTAIONS_PATH,
                key=TRAIN_ANNOTATION_FILE_NAME,
            )
            logger.info("Downloaded train annotation file from s3 bucket")

            self.s3.download_file(
                bucket_name=BUCKET_NAME,
                output_file_path=self.model_trainer_config.TEST_ANNOTAIONS_PATH,
                key=TEST_ANNOTATION_FILE_NAME,
            )
            logger.info("Downloaded test annotation file from s3 bucket")

            train_annotations_local_path = os.path.join(
                from_root(), TRAIN_ANNOTATION_FILE_NAME
            )
            test_annotations_local_path = os.path.join(
                from_root(), TEST_ANNOTATION_FILE_NAME
            )

            train_data = self.utils.load_json(
                json_file_path=train_annotations_local_path
            )
            test_data = self.utils.load_json(json_file_path=test_annotations_local_path)
            logger.info("Loaded train data and test data")

            prepared_train_data_local_path = os.path.join(
                ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR, SPACY_TRAIN_DATA_FORMAT_NAME
            )
            prepared_test_data_local_path = os.path.join(
                ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR, SPACY_TEST_DATA_FORMAT_NAME
            )

            self.create_spacy_format_data(
                data=train_data,
                docbin_obj=db,
                output_file_path=prepared_train_data_local_path,
                nlp_model=nlp,
            )
            self.create_spacy_format_data(
                data=test_data,
                docbin_obj=db,
                output_file_path=prepared_test_data_local_path,
                nlp_model=nlp,
            )
            logger.info("Converted train and test data into spacy format.")

            # Downloading the config file for training
            config_file_path = os.path.join(from_root(), CONFIG_FILE_NAME)
            os.system(
                f"python3 -m spacy init config {config_file_path} --lang en --pipeline ner --optimize efficiency"
            )

            # Training
            best_model_path = os.path.join(ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR)
            os.system(
                f"python3 -m spacy train {config_file_path} --output {best_model_path} --paths.train {prepared_train_data_local_path} --paths.dev {prepared_test_data_local_path}"
            )
            logger.info("Model training Done...!!")

            best_model_local_path = os.path.join(ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR, BEST_MODEL_FOLDER_NAME)         
            self.s3.sync_folder_to_s3(folder=best_model_local_path,bucket_folder_name=BEST_MODEL_FOLDER_NAME,bucket_name=BUCKET_NAME)          
            logger.info("Best model uploaded to s3 bucket.")

            model_trainer_artifacts = ModelTrainerArtifacts(best_model_path=best_model_local_path)

            logger.info(
                "Exited the initiate_model_trainer method of Model trainer class"
            )
            return model_trainer_artifacts

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
