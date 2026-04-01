import os,sys;

from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.dataValidationConfig import DataValidationConfig;
from networksecurity.utils.yamlFileUtil import read_schema_yaml,save_yaml_file;
from networksecurity.utils.csvFileUtil import read_csv;
import pandas as pd;
from scipy.stats import ks_2samp;


class DataValidation:
    ##### This class is responsible for performing data validation
    def __init__(self):
        #### Constructor
        try:
            self.__config=DataValidationConfig();
            # print(self.__config.data_drift_file_path);
            # print(self.__config.data_validation_dir);
            # print(self.__config.schema_filepath);
            self.__schemaConfig=read_schema_yaml(self.__config.schema_filepath)
            # print(self.__schemaConfig)
        except Exception as e:
            raise CustomException(e,sys)
        
    def validate_no_of_columns(self,df:pd.DataFrame)->bool:
        #### This method eis responsible for validate the coulmns of the dataframe
        try:
            not_found_cols=[];
            status=True;
            logging.info("starting count check for input columns")
            input_column_count=len(df.columns)
            schema_file_column_count=len(self.__schemaConfig['columns'])
            logging.info(f"input file column count {input_column_count}")
            logging.info(f"schema file column count {schema_file_column_count}")
            for column in self.__schemaConfig['columns']:
                for key in column.keys():
                    if key not in df.columns:
                        not_found_cols.append(column.keys());
                        status=False;

            if input_column_count==schema_file_column_count and status==True:
                logging.info("Column count matches with schema file")
                logging.info("Check for input columns completed")
                return True;
            else:
                logging.info("Column count not matches with schema file")
                logging.info("Check for input columns completed")
                logging.info(f"columns {not_found_cols} not found")
                return False;
        except Exception as e:
            raise CustomException(e,sys)

    def validate_numerical_columns(self,df:pd.DataFrame)->bool:
        try:
            not_numerical_cols=[];
            status=True;
            logging.info("starting numerical columns check")
            num_cols=[column for column in df.columns if df[column].dtype!='O']
            input_numerical_column_count=len(num_cols)
            schema_file_numerical_column_count=len(self.__schemaConfig['numeric_columns'])
            logging.info(f"input file numerical column count {input_numerical_column_count}")
            logging.info(f"schema file numerical column count {schema_file_numerical_column_count}")
            for column in self.__schemaConfig['numeric_columns']:
                if column not in num_cols:
                    not_numerical_cols.append(column);
                    status=False;

            if input_numerical_column_count==schema_file_numerical_column_count and status==True:
                logging.info("Numerical Column count matches with schema file")
                logging.info("check for numeric input columns completed")
                return True;
            else:
                logging.info("Numerical Column count not matches with schema file")
                logging.info("check for numeric input columns completed")
                logging.info(f"columns {not_numerical_cols} not numerical")
                return False;
        except Exception as e:
            raise CustomException(e,sys)

    def data_drift_check(self,base_df:pd.DataFrame,comp_df:pd.DataFrame,thresold:float)->bool:
        ##### This function is responsibel for data drift check
        try:
            report={};
            isfound=True;
            logging.info("Starting data drift check")
            for column in base_df.columns:
                df1=base_df[column]
                df2=comp_df[column]
                score=ks_2samp(df1,df2)
                if thresold<=score.pvalue:
                    isfound=False;
                else:
                    isfound=True;
                report[column]={
                    "pvalue": float(score.pvalue),
                    "isFound": isfound
                };
            save_yaml_file(report,self.__config.data_drift_file_path)
            logging.info("completed data drift check")
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_validation(self,train_filepath:str,test_filepath:str):
        #### This method is responsible for performing all the data validations
        try:
            logging.info("Starting Data validation")
            logging.info("Reading Data from train csv started")
            train_df=read_csv(filepath=train_filepath);
            logging.info(f"shape of train df {train_df.shape}")
            logging.info("Reading Data from train csv successfull")
            logging.info("Reading Data from test csv started")
            test_df=read_csv(filepath=test_filepath);
            logging.info(f"shape of test df {test_df.shape}")
            logging.info("Reading Data from test csv successfull")
            


            logging.info("checking columns  for  train csv is started")
            train_clomunCheckstatus=self.validate_no_of_columns(train_df) and self.validate_numerical_columns(train_df)
            logging.info("checking column  for  train csv is completed")
            logging.info("checking column  for  test csv is started")
            test_clomunCheckstatus=self.validate_no_of_columns(test_df) and self.validate_numerical_columns(test_df)
            logging.info("checking column  for  test csv is completed")

            os.makedirs(self.__config.data_validation_dir,exist_ok=True)
            if train_clomunCheckstatus and test_clomunCheckstatus:
                self.data_drift_check(train_df,test_df,.95)

        except Exception as e:
            raise CustomException(e,sys)