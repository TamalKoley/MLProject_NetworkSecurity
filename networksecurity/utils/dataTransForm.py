import os;
import sys;
import json;
from dotenv import load_dotenv;
import pandas as pd;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from typing import Dict;


load_dotenv()

class DataTransformtoJSON():
    #### This class is created for parsing csv data 
    def __init__(self):
         #### Constructor
        self.__CSV_FILE=os.getenv('CSV_FILE_PATH')
    
    def Transform(self)->Dict:
        #### This function is created for parsing csv data
        try:
            logging.info('Data Transformation started')
            df=pd.read_csv(self.__CSV_FILE);
            df.reset_index(drop=True,inplace=True)
            jsonData=list(json.loads(df.T.to_json()).values())
            logging.info('Data Transformation compeleted')
            return jsonData
        except Exception as e:
            raise CustomException(e,sys);