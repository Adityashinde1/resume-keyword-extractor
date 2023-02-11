import os
import sys
import cv2
import spacy
import pytesseract
from resume_keyword.configuration.s3_operations import S3Operation
from resume_keyword.entity.config_entity import ModelPredictorConfig
from resume_keyword.exception import ResumeKeywordException
import logging
from pdf2image import convert_from_path
from resume_keyword.constants import *

logger = logging.getLogger(__name__)


class ModelPredictor:
    def __init__(self) -> None:
        self.S3_operation = S3Operation()
        self.model_predictor_config = ModelPredictorConfig()


    def get_model_from_s3(self, folder: str, bucket_name: str, bucket_folder_name: str):
        try:
            logger.info("Entered the get_model_from_s3 method of Model predictor class")
            self.S3_operation.sync_folder_from_s3(folder=folder, bucket_name=bucket_name, bucket_folder_name=bucket_folder_name)
            logger.info("Got the best model from s3")
            logger.info("Exited the get_model_from_s3 method of Model predictor class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e


    def pdf_to_img(self, pdf_file_path: str) -> None:
        try:
            logger.info("Entered the pdf_to_img method of Data transformation class")
            os.makedirs(os.path.join(self.model_predictor_config.MODEL_PREDICTOR_ARTIFACTS_DIR, PDF_TO_IMG_DIR), exist_ok=True)
            # Store Pdf with convert_from_path function
            images = convert_from_path(pdf_file_path)
            for i in range(len(images)):
                fname = os.path.join(
                        self.model_predictor_config.MODEL_PREDICTOR_ARTIFACTS_DIR,
                        PDF_TO_IMG_DIR,
                        f"image_{str(i)}.jpg",
                    )
                images.save(fname)

            logger.info("Exited the pdf_to_img method of Data transformation class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    def img_to_txt(self, img_pdf_folder_path: str) -> None:
        try:
            logger.info("Entered the img_to_txt method of Data transformation class")

            os.makedirs(os.path.join(self.model_predictor_config.MODEL_PREDICTOR_ARTIFACTS_DIR, IMG_TO_TXT_DIR), exist_ok=True)

            for i, resume in enumerate(os.listdir(img_pdf_folder_path)):
                img = cv2.imread(img_pdf_folder_path + "/" + resume)
                img = cv2.resize(img, (1000, 1100))
                text = pytesseract.image_to_string(img)

                fname = os.path.join(f"image_txt_{str(i)}.txt")
                with open(fname, "w", encoding='utf-8') as file:
                    file.write(text)

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e


    def initiate_model_predictor(self, filename: str):
        try:
            logger.info("Entered the initiate_model_predictor method of Model predictor class.")

            os.makedirs(self.model_predictor_config.MODEL_PREDICTOR_ARTIFACTS_DIR, exist_ok=True)
            logger.info(
                f"Created {os.path.basename(self.model_predictor_config.MODEL_PREDICTOR_ARTIFACTS_DIR)} directory."
            )

            s3_model_download_path = os.path.join(from_root(), BEST_MODEL_FOLDER_NAME)
            self.get_model_from_s3(folder=s3_model_download_path, bucket_name=BUCKET_NAME, bucket_folder_name=BEST_MODEL_FOLDER_NAME)

            self.pdf_to_img(pdf_file_path=filename)

            img_pdf_folder_path = os.path.join(ARTIFACTS_DIR, MODEL_PREDICTOR_ARTIFACTS_DIR, IMG_TO_TXT_DIR)
            self.img_to_txt(img_pdf_folder_path=img_pdf_folder_path)

            nlp_ner = spacy.load(s3_model_download_path)

            
            

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

