import sys;
import os;
from dotenv import load_dotenv;
from networksecurity.logger.logger import logging;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.Database.DBFunction import DataBaseConnection;
from networksecurity.utils.dataTransForm import DataTransformtoJSON;

if __name__=='__main__':
    ###### This code is responsible for extarcting the data from csv and then load it to MongoDB in a JSON format.
    try:
        logging.info('Starting ETL pipeline')
        load_dotenv()
        dataBaseName=os.getenv('DB_NAME')
        dbCollectionName=os.getenv('COLLECTION_NAME')
        logging.info("Program Started")
        dt=DataTransformtoJSON()
        jsondata=dt.Transform()
        db=DataBaseConnection()
        db.connect()
        db.load(DatabaseName=dataBaseName,CollectionName=dbCollectionName,jsonData=jsondata)
        logging.info('ETL pipeline successfully completed')
    except CustomException as e:
        logging.info(e)
    finally: 
        db.disconnect();