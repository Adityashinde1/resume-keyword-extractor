from resume_keyword.pipeline.prediction_pipeline import ModelPredictor
from resume_keyword.exception import ResumeKeywordException
import sys

def prediction():
    try:
        model_predictor = ModelPredictor()

        model_predictor.initiate_model_predictor(filename='/content/resume_194.pdf')

    except Exception as e:
        raise ResumeKeywordException(e, sys) from e
    

if __name__ == "__main__":
    prediction()