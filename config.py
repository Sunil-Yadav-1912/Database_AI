import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
S3_FOLDER_PATH = os.getenv("S3_FOLDER_PATH")
AWS_ACCESS_KEY=os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY=os.getenv("AWS_SECRET_KEY")
API_KEY=os.getenv("API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")
TEMPERATURE=os.getenv("TEMPERATURE")
DB_HOST=os.getenv("DB_HOST")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_PORT=os.getenv("DB_PORT")
TRAINING_SHEET=os.getenv("TRAINING_SHEET")
LOGO=os.getenv("LOGO")