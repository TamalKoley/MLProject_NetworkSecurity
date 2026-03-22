import os;
import sys;
from pymongo import MongoClient;
from dotenv import load_dotenv;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from typing import Dict;

load_dotenv()

class DataBaseConnection():
    ##### This class is responsible for creating and closing Mongodb connection and data load
    def __init__(self):
        self.__DB_URL=os.getenv('MONGODB_URL')
        self.__client:MongoClient=None;

    def connect(self):
         ##### This function is responsible for creating MongoDB connection
        try:
            if (self.__client):
                logging.info('already have a active connection')
 
            else:
                self.__client=MongoClient(self.__DB_URL)
                result=self.__client.admin.command('ping')

                if 'ok' in result:
                    logging.info('MongoDB connection cerated succesfully')

        except Exception as e:
            raise CustomException(e,sys)
    
    def disconnect(self):
        ##### This function is responsible for closing  MongoDB connection
        try:
            if (self.__client):
                logging.info('MongoDB connection Closed Successfully')
            else:
                logging.info('No active connection')
        except Exception as e:
            raise CustomException(e,sys)
        
    def load(self,DatabaseName,CollectionName,jsonData):
        ##### This function is responsible for loading data into   MongoDB 
        try:
            if (self.__client):
                logging.info('Starting data load')
                db=self.__client[DatabaseName]
                collection=db[CollectionName]
                collection.insert_many(jsonData)
                logging.info('Data load completed')
            else:
                logging.info('No active connection , create a active connection at first')
        except Exception as e:
            raise CustomException(e,sys)
        
    def export(self,DatabaseName,CollectionName)->Dict:
        try:
            if (self.__client):
                logging.info('Starting data export')
                db=self.__client[DatabaseName]
                data=db[CollectionName]
                logging.info('data export Completed')
                return data
                
        except Exception as e:
            raise CustomException(e,sys)


