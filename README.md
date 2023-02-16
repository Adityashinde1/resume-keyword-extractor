# resume-keyword-extractor

## Problem statement
With the rapid growth of Internet-based recruiting, there are a great number of personal resumes among recruiting systems. To gain more attention from the recruiters, most resumes are written in diverse formats, including varying font size, font colour, and table cells. Yet, it is quite challenging to personally review each resume and match the requisite skills. Automate the procedure and take steps to pull the skills from the resume.

## Solution proposed
PDF files were used as the data source for this project. First, using the pdf2image library, pdf files were transformed into images. then tesseract ocr was used to extract the text from those images. All text files are combined into one text file for NER annotation after the text has been extracted. The Spacy model has been trained for the NER task. The email and skills have been added to the MongoDB database after extraction.

## Dataset used
For this project pdf file data has been used. From the organization's database, all of the pdf files were taken.

## Teck stack used
1. Python 
2. FastAPI
3. Deep learning
4. Coputer vision
5. Natural language processing
6. Docker

## Infrastructure required
1. AWS S3
2. AWS EC2 instance

## How to run
Step 1. You need to create an instance in AWS (Any instance >= t2.medium). Connect to your instance and open terminal

Step 2. Cloning the repository
```
git clone https://github.com/Deep-Learning-01/resume-keyword-extractor.git
```
Step 3. Download and install AWS CLI 
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && sudo ./aws/install
```
Step 4. Configure AWS credentials with following command
```
aws configure
```
Step 5. Export MongoDB URL
```
export MONGO_URL=<'your_mongodb_url'>
```
Step 6. Install the poppler utils necessary for py2pdf library
```
apt-get install -y poppler-utils
```
Step 7. Install tesseract-ocr
```
apt install tesseract-ocr -y
```
Step 8. In AWS instance we have to download python3 package
```
apt install python3-pip
```
Step 9. Install openCV library 
```
apt-get install python3-opencv
```
Step 10. Change the directory to resume-keyword-extractor
```
cd resume-keyword-extractor
```
Step 11. Install necessary requirements
```
pip3 install -r requirements.txt
```
Step 12. To train the model
```
python3 train.py
```
Step 13. To predict
```
python3 app.py
```

## Run locally
In this project only prediction endpoint is dockerized 

1. Check if the Dockerfile is available in the project directory.
2. Build the Docker image.
```
docker build -t <image_name> .
```
3. Run the docker image
```
docker run -d -e MONGO_URL=<your_mongodb_url> -e AWS_ACCESS_KEY_ID=<aws_access_key> -e AWS_SECRET_ACCESS_KEY=<aws_secret_access_key> -e AWS_DEFAULT_REGION=<aws_region> -p 8000:8000 <image_name>
```

## `resume_keyword` is the main package folder which contains -
**Components** : Contains all components of this Project
- DataIngestion
- DataTransformation
- ModelTrainer

**Custom Logger and Exceptions** are used in the Project for better debugging purposes.

## Conclusion
The ed-tech firms can make use of this project. With the help of this project, a company can screen the results based on the customer's candidate needs and send the CV of a candidate who matches those requirements directly to the client.
