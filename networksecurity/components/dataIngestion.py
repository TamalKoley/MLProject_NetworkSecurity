import sys;
import os;
import pandas as pd;
from sklearn.model_selection import train_test_split;
from typing import Tuple;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.dataIngestionConfig import DataIngestionConfig;
from networksecurity.Database.DBFunction import DataBaseConnection;



class DataIngestion:
    #### This class is responsible for exporting data from MongoDB and save it in csv format then split into train test and save it in CSV format
    def __init__(self):
        #### Constructor
        try:
            self.__config:DataIngestionConfig=DataIngestionConfig()
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_dataingestion(self)->Tuple[str,str]:
        ##### This function will peform all the steps required for data ingestion with the help of other functions
        try:
            logging.info('Starting Data ingestion')
            os.makedirs(self.__config.ingestion_path,exist_ok=True)
            os.makedirs(self.__config.feature_path,exist_ok=True)
            db=DataBaseConnection()
            db.connect()
            jsonData=db.export(self.__config.database_name,self.__config.db_collection_name)
            df=pd.DataFrame(list(jsonData.find()))
            df.drop(columns=["_id"],axis=1,inplace=True)
            logging.info('Saving feature Data')
            self.save_tocsv(df,self.__config.feature_filepath)
            logging.info('Feature Data saved')
            train_data,test_data=train_test_split(df,test_size=self.__config.train_test_percentage,random_state=42)
            logging.info('Saving train and test  Data')
            self.save_tocsv(train_data,self.__config.ingestion_train_filepath)
            self.save_tocsv(test_data,self.__config.ingestion_test_filepath)
            logging.info('train and test  Data saved')
            logging.info('Data ingestion Completed')
            return(
                self.__config.ingestion_train_filepath,
                self.__config.ingestion_test_filepath
            )
        except Exception as e:
            raise CustomException(e,sys)

    def save_tocsv(self,data:pd.DataFrame,filepath):
        ##### This function will save the data into csv format
        try:
            logging.info('csv saving is in progress')
            data.to_csv(filepath,index=False,header=True)
            logging.info('csv is saved successfully')
        except Exception as e:
            raise CustomException(e,sys)

     