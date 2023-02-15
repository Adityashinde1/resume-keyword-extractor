import os
from from_root import from_root
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from uvicorn import run as app_run
from resume_keyword.pipeline.prediction_pipeline import ModelPredictor
from resume_keyword.constants import *

app = FastAPI()

predictor = ModelPredictor()

@app.post("/predict")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = os.path.join(from_root(), uploaded_file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    result = predictor.initiate_model_predictor(uploaded_file.filename)

    return JSONResponse(content=result, status_code=200)


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=PORT)