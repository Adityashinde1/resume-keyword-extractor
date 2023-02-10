import os
import sys
from resume_keyword.exception import ResumeKeywordException
from resume_keyword.pipeline.train_pipeline import TrainPipeline

from resume_keyword.constants import *


def training():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

    except Exception as e:
        raise ResumeKeywordException(e, sys) from e


if __name__ == "__main__":
    training()