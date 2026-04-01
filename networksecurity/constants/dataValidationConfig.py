import os;
import sys;
from networksecurity.logger.logger import logging;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.constants.datetimeConfig import datetimestmp;

class DataValidationConfig:
    #### this class is responsible for creating constants for data validation
    def __init__(self):
        #### Constructor
        try:
            logging.info("Starting Config setup for Data Validation");
            ARTIFACT_DIR="Artifacts";
            DATA_VALIDATION_DIR="DataValidation";
            DATA_DRIFT_FILE="drift_report.yaml";
            SCHEMA_DIR="Schema";
            SCHEMA_FILE="inputDataSchema.yaml"
            TIMESTAMP=datetimestmp;
            self.data_validation_dir=os.path.join(ARTIFACT_DIR,TIMESTAMP,DATA_VALIDATION_DIR);
            self.data_drift_file_path=os.path.join(ARTIFACT_DIR,TIMESTAMP,DATA_VALIDATION_DIR,DATA_DRIFT_FILE);
            self.schema_filepath=os.path.join(SCHEMA_DIR,SCHEMA_FILE)
            logging.info("Config setup for Data Validation is completed");
            
        except Exception as e:
            raise CustomException(e,sys);