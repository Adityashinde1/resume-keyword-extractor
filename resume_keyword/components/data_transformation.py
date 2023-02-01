import os
import sys
import logging
import cv2
import pytesseract
from resume_keyword.constants import *
from pdf2image import convert_from_path
from resume_keyword.configuration.s3_operations import S3Operation
from resume_keyword.exception import ResumeKeywordException
from resume_keyword.entity.config_entity import DataTransformationConfig
from resume_keyword.entity.artifacts_entity import DataTransformationArtifacts, DataIngestionArtifacts

pytesseract.pytesseract.tesseract_cmd=TESSERACT_CMD

logger = logging.getLogger(__name__)


class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig, data_ingestion_artifacts: DataIngestionArtifacts, s3_opearations: S3Operation) -> None:
        self.data_transformation_config = data_transformation_config
        self.data_ingestion_artifacts = data_ingestion_artifacts
        self.s3_opearations = s3_opearations


    def pdf_to_img(self, pdf_folder_path: str, poppler_path: str, pdf_img_folder_path: str) -> None:
        try:
            logger.info("Entered the pdf_to_img method of Data transformation class")

            os.makedirs(os.path.join(pdf_img_folder_path),exist_ok=True)
            logger.info(f"Created {os.path.basename(pdf_folder_path)} Directory.")

            for i,pdf in enumerate(os.listdir(pdf_folder_path)):
                images = convert_from_path(pdf_folder_path + "/" + pdf,500,poppler_path=poppler_path)
                for image in images:
                    fname = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,PDF_IMAGES_FOLDER_NAME,f"image_{str(i)}.jpg")
                    image.save(fname)
            logger.info("Images saved to artifacts directory.")
            logger.info("Exited the pdf_to_img method of Data transformation class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e


    def img_to_txt(self, txt_folder_path: str, img_pdf_folder_path: str) -> None:
        try:
            logger.info("Entered the img_to_txt method of Data transformation class")

            os.makedirs(os.path.join(txt_folder_path),exist_ok=True)
            logger.info(f"Created {os.path.basename(txt_folder_path)} Directory.")

            for i, resume in enumerate(os.listdir(img_pdf_folder_path)):
                img = cv2.imread(img_pdf_folder_path + "/" + resume)
                img = cv2.resize(img, (1000, 1100))
                text = pytesseract.image_to_string(img)

                fname = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,RESUME_TXT_FILE_FOLDER_NAME,f"image_txt_{str(i)}.txt")
                with open(fname, 'w') as file:
                    file.write(text)

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
        

    def concatenate_txt_file(self, txt_files_path: str, output_txt_file_path: str) -> None:
        try:
            logger.info("Entered the concatenate_txt_file method of Data transformation class")

            read_files = os.listdir(txt_files_path)
            with open(output_txt_file_path, "wb") as outfile:
                for f in read_files:
                    with open(txt_files_path + '/' + f, 'rb') as infile:
                        outfile.write(infile.read())

                outfile.close()

            logger.info("Exited the concatenate_txt_file method of Data transformation class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifacts:
        try:
            logger.info("Entered the initiate_data_transformation method of Data transformation class")

            # Creating Data Transformation Artifacts directory inside artifact folder
            os.makedirs(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR, exist_ok=True)
            logger.info(
                f"Created {os.path.basename(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR)} directory."
            )
            print(" Started conversion of PDF to images >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            pdf_img_folder_path = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,PDF_IMAGES_FOLDER_NAME)
            pdf_folder_path = self.data_ingestion_artifacts.pdf_folder_path
            self.pdf_to_img(pdf_folder_path=pdf_folder_path, poppler_path=POPPLER_PATH, pdf_img_folder_path=pdf_img_folder_path)
            print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Converted PDF files to Images >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            logger.info("Converted pdf files to images.")

            print(" Started conversion of Images to txt files >>>>>>>>>>>>>>>>>>>>>>>>>")
            txt_folder_path = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,RESUME_TXT_FILE_FOLDER_NAME)
            img_pdf_folder_path = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR,PDF_IMAGES_FOLDER_NAME)
            self.img_to_txt(txt_folder_path=txt_folder_path, img_pdf_folder_path= img_pdf_folder_path)
            print("<<<<<<<<<<<<<<<<<<< Converted Images to txt files >>>>>>>>>>>>>>>>>>>>>>>>>")
            logger.info("Converted Images to txt files.")

            txt_files_path = os.path.join(self.data_transformation_config.DATA_TRANSFORMATION_ARTIFACTS_DIR, RESUME_TXT_FILE_FOLDER_NAME)
            self.concatenate_txt_file(txt_files_path=txt_files_path, output_txt_file_path=self.data_transformation_config.TXT_FILE_PATH)
            logger.info("Genarated one txt file for annotations.")

            self.s3_opearations.upload_file(from_filename=self.data_transformation_config.TXT_FILE_PATH, to_filename=TXT_FILE_NAME, 
                                            bucket_name=BUCKET_NAME,remove=False)
            logger.info("Txt file uploaded to s3 bucket for annotations")

            data_transformation_artifacts = DataTransformationArtifacts(resume_pdf_images_path=pdf_img_folder_path,
                                                                        resume_txt_files_path=txt_folder_path,
                                                                        txt_filepath=self.data_transformation_config.TXT_FILE_PATH)
            logger.info("Exited the initiate_data_transformation method of Data transformation class")

            return data_transformation_artifacts

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e