import os,sys;
import numpy as np;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.datetimeConfig import datetimestmp


class DataTransformationConfig:
    #### This class is responsible for config setup required for Data Transformation
    def __init__(self):
        try:
            logging.info('starting Data Transformation config setup')
            TIMESTAMP=datetimestmp;
            transformer_file='transformer_model.pkl'
            transformer_dir='Data_Transformation'
            artifact_dir="Artifacts"
            transformed_dir="Transformed"
            transformed_train_file="transformed_train_file.npy"
            transformed_test_file="transformed_test_file.npy"

            self.trasformer_filedir=os.path.join(artifact_dir,TIMESTAMP,transformer_dir)
            self.trasformer_filepath=os.path.join(artifact_dir,TIMESTAMP,transformer_dir,transformer_file)
            self.target_column="Result";
            self.transformed_dir=os.path.join(artifact_dir,TIMESTAMP,transformer_dir,transformed_dir)
            self.transformed_test_filepath=os.path.join(artifact_dir,TIMESTAMP,transformer_dir,transformed_dir,transformed_test_file)
            self.transformed_train_filepath=os.path.join(artifact_dir,TIMESTAMP,transformer_dir,transformed_dir,transformed_train_file)
            self.imputer_config={
                "missing_values": np.nan,
                "n_neighbors": 3,
                "weights" : "uniform"
            };
            logging.info('Data Transformation config setup Completed')
        except Exception as e:
            raise CustomException(e,sys)