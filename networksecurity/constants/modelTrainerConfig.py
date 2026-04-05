import os,sys;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.datetimeConfig import datetimestmp;

class ModelTrainerConfig:
    ##### This class is responsible for creating the configurations required for model training
    def __init__(self):
        ### Constructor
        try:
            logging.info('Starting Model Trainer Config Setting')
            ARTIFACT_DIR="Artifacts"
            TIMESTAMP=datetimestmp
            MODEL_TRAINING_DIR="Model_Training"
            TRANSFORMED_OBJECT_DIR="Transformed_Object"
            MODEL_FILE_NAME="trained_model.pkl"
            HYP_TUNNING_RESULT_FILE="hyperparameter_tuning_result.yaml"
            CLASSIFICATION_REPORT_FILENAME="classification_report.yaml"
            self.model_training_dir=os.path.join(ARTIFACT_DIR,TIMESTAMP,MODEL_TRAINING_DIR)
            self.hyp_result_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,MODEL_TRAINING_DIR,HYP_TUNNING_RESULT_FILE)
            self.classification_report_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,MODEL_TRAINING_DIR,CLASSIFICATION_REPORT_FILENAME)
            self.transformed_object_dir=os.path.join(ARTIFACT_DIR,TIMESTAMP,MODEL_TRAINING_DIR,TRANSFORMED_OBJECT_DIR)
            self.transformed_model_filepath=os.path.join(ARTIFACT_DIR,TIMESTAMP,MODEL_TRAINING_DIR,TRANSFORMED_OBJECT_DIR,MODEL_FILE_NAME)
            logging.info('Model Trainer Config Setting Completed')
        except Exception as e:
            raise CustomException(e,sys)