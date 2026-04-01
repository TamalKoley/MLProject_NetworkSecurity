import os,sys;
import pandas as pd;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;

def read_csv(filepath:str)->pd.DataFrame:
    try:
        logging.info("Starting data reading from csv file");
        dataFrame=pd.read_csv(filepath);
        logging.info("Data reading from csv file is successfull");
        return dataFrame;
    except Exception as e:
        raise CustomException(e,sys)
