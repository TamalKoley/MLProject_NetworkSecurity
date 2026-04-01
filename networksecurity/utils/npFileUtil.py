import os,sys;

import numpy as np;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;

def save_numpyArray_data(filepath:str,data:np.ndarray):
    #### This function saves np array data into npy format.
    try:
        logging.info("Starting save numpy array data")
        np.save(filepath,data)
        logging.info("Numpy array data saved")
    except Exception as e:
        raise CustomException(e,sys)