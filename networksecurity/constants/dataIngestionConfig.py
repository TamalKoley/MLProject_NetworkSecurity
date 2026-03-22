import os;
import sys;
from dotenv import load_dotenv;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from datetime import datetime;

class DataIngestionConfig:
    ##### This class is created to define all the constant values required for data ingestion

    def __init__(self):
        try:
            logging.info('Starting Data ingestion config setup')
            load_dotenv();
            TIMESTAMP=datetime.now().strftime('%Y%m%d_%H%M%S')
            ARTIFACT_DIR="Artifacts"
            INGESTION_DIR="Ingested"
            FEATURE_DIR="Feature"
            INGESTION_TEST_FILE="test.csv"
            INGESTION_TRAIN_FILE="train.csv"
            FEATURE_FILE="raw_data.csv"
            self.ingestion_path=os.path.join(ARTIFACT_DIR,TIMESTAMP,INGESTION_DIR)
            self.feature_path=os.path.join(ARTIFACT_DIR,TIMESTAMP,FEATURE_DIR)
            self.ingestion_test_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,INGESTION_DIR,INGESTION_TEST_FILE)
            self.ingestion_train_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,INGESTION_DIR,INGESTION_TRAIN_FILE)
            self.feature_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,FEATURE_DIR,FEATURE_FILE)
            self.database_name=os.getenv('DB_NAME')
            self.db_collection_name=os.getenv('COLLECTION_NAME')
            self.target_name="Result"
            self.train_test_percentage=0.25
            logging.info('Data ingestion config setup Completed')

        except Exception as e:
            raise CustomException(e,sys)