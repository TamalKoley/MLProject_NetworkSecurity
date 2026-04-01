import sys;
import os;
from dotenv import load_dotenv;
from networksecurity.logger.logger import logging;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.components.dataIngestion import DataIngestion;
from networksecurity.components.dataValidation import DataValidation;
from networksecurity.components.dataTransformation import DataTransformation;


if __name__=='__main__':
    try:
        logging.info('Main Program Started')
        di=DataIngestion()
        train_filepath,test_filepath=di.initiate_dataingestion();
        # print(train_filepath)
        # print(test_filepath)
        dv=DataValidation()
        dv.initiate_data_validation(test_filepath=test_filepath,train_filepath=train_filepath)
        dt=DataTransformation();
        dt.initiate_dataTransformation(train_filepath=train_filepath,test_filepath=test_filepath)
        logging.info('Main Program Completed')
        
    except CustomException as e:
        logging.info(e)
