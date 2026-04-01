import os,sys;

import pickle;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;


def save_pickle_file(filepath:str,data):
    ##### This functions saves data into pickle file
    try:
        logging.info("Starting data save in pickle format")
        with open(filepath,'wb') as file:
            pickle.dump(data,file=file);
        logging.info("data saved in pickle format")
    except Exception as e:
        raise CustomException(e,sys)