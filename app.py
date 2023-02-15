import os
from from_root import from_root
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response, JSONResponse
from uvicorn import run as app_run
from resume_keyword.pipeline.prediction_pipeline import ModelPredictor
from resume_keyword.constants import *
import json

app = FastAPI()

predictor = ModelPredictor()

@app.post("/predict")
async def create_upload_file(uploaded_file: UploadFile = File(...)):
    file_location = os.path.join(from_root(), uploaded_file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(uploaded_file.file.read())

    skills = predictor.initiate_model_predictor(uploaded_file.filename)

    json_str = json.dumps(skills, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=PORT)
