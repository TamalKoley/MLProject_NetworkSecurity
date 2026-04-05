import os,sys;

import pickle;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;


def save_pickle_file(filepath:str,data):
    ##### This function saves data into pickle file
    try:
        logging.info("Starting data save in pickle format")
        with open(filepath,'wb') as file:
            pickle.dump(data,file=file);
        logging.info("data saved in pickle format")
    except Exception as e:
        raise CustomException(e,sys)
    
def  load_pickle_file(filepath:str):
    ###### This function will load a pickle file
    try:
        logging.info("Starting data load from pickle file")
        with open(filepath,'rb') as file:
            data=pickle.load(file)
        logging.info("Data load from pickle file is completed")
        return data;
    except Exception as e:
        raise CustomException(e,sys)