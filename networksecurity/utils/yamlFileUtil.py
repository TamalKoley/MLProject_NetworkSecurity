import os,sys;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
import yaml;
from typing import Dict;

def read_schema_yaml(filepath:str)->Dict:
    #### This function is responsible for reading the schema yaml file for input data.
    try:
        logging.info('Starting schema file reading')
        with open(filepath,'rb') as file:
            data= yaml.safe_load(file)
        logging.info('Schema file reading completed')
        return data;
    except Exception as e:
        raise CustomException(e,sys)

def save_yaml_file(data,filepath:str):
    #### This function is responsible for saving drift report in a yaml format
    try:
        logging.info("saving data in yaml format")
        with open(filepath,'w') as file:
            yaml.dump(data,file)
        logging.info("saving data in yaml format is completed")
    except Exception as e:
        raise CustomException(e,sys)