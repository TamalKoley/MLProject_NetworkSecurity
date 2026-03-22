import sys;
import os;
from dotenv import load_dotenv;
from networksecurity.logger.logger import logging;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.components.dataIngestion import DataIngestion;


if __name__=='__main__':
    try:
        logging.info('Main Program Started')
        di=DataIngestion()
        train_filepath,test_filepath=di.initiate_dataingestion();
        print(train_filepath)
        print(test_filepath)
        logging.info('Main Program Completed')
    except CustomException as e:
        logging.info(e)
