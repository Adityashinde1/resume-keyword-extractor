import shutil
import sys
from typing import Dict
import dill
import pickle
import json
import yaml
from zipfile import Path
from resume_keyword.constants import *
from resume_keyword.exception import ResumeKeywordException
import logging

# initiatlizing logger
logger = logging.getLogger(__name__)


class MainUtils:
    def read_yaml_file(self, filename: str) -> Dict:
        logger.info("Entered the read_yaml_file method of MainUtils class")
        try:
            with open(filename, "rb") as yaml_file:
                return yaml.safe_load(yaml_file)

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def dump_pickle_file(output_filepath: str, data) -> None:
        try:
            with open(output_filepath, "wb") as encoded_pickle:
                pickle.dump(data, encoded_pickle)

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def load_pickle_file(filepath: str) -> object:
        try:
            with open(filepath, "rb") as pickle_obj:
                obj = pickle.load(pickle_obj)
            return obj

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def save_object(file_path: str, obj: object) -> None:
        logger.info("Entered the save_object method of MainUtils class")
        try:
            with open(file_path, "wb") as file_obj:
                dill.dump(obj, file_obj)

            logger.info("Exited the save_object method of MainUtils class")

            return file_path

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def load_object(file_path: str) -> object:
        logger.info("Entered the load_object method of MainUtils class")
        try:
            with open(file_path, "rb") as file_obj:
                obj = dill.load(file_obj)
            logger.info("Exited the load_object method of MainUtils class")
            return obj

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def create_artifacts_zip(file_name: str, folder_name: str) -> None:
        logger.info("Entered the create_artifacts_zip method of MainUtils class")
        try:
            shutil.make_archive(file_name, "zip", folder_name)
            logger.info("Exited the create_artifacts_zip method of MainUtils class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def unzip_file(filename: str, folder_name: str) -> None:
        logger.info("Entered the unzip_file method of MainUtils class")
        try:
            shutil.unpack_archive(filename, folder_name)
            logger.info("Exited the unzip_file method of MainUtils class")

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def read_txt_file(filename: str) -> str:
        logger.info("Entered the read_txt_file method of MainUtils class")
        try:
            # Opening file for read only
            file1 = open(filename, "r", encoding='utf-8')
            # read all text
            text = file1.read()
            # close the file
            file1.close()
            logger.info("Exited the read_txt_file method of MainUtils class")
            return text

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def save_txt_file(output_file_path: str, data: list) -> Path:
        logger.info("Entered the save_txt_file method of MainUtils class")
        try:
            with open(output_file_path, "w") as file:
                file.writelines("% s\n" % line for line in data)

            logger.info("Exited the save_txt_file method of MainUtils class")
            return output_file_path

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e

    @staticmethod
    def load_json(json_file_path: str) -> None:
        logger.info("Entered the load_json method of MainUtils class")
        try:
            f = open(json_file_path, encoding = 'utf-8')
            data = json.load(f)

            logger.info("Exited the load_json method of MainUtils class")
            return data

        except Exception as e:
            raise ResumeKeywordException(e, sys) from e
