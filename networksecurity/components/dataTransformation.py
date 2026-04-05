import os,sys;
import numpy as np;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;
from networksecurity.constants.dataTransformationConfig import DataTransformationConfig;
from  networksecurity.utils.csvFileUtil import read_csv;
from networksecurity.utils.npFileUtil import save_numpyArray_data;
from networksecurity.utils.pickleFileUtil import save_pickle_file;
from sklearn.pipeline import Pipeline;
from sklearn.impute import KNNImputer;
from typing import Tuple;

class DataTransformation:
    ## This class is responsible for train  and test data transformation
    def __init__(self):
        ## Constructor
        try:
            self.__config=DataTransformationConfig()

        except Exception as e:
            raise CustomException(e,sys)
        
    def get_transformer(self)->Pipeline:
        ### this method  is responsible for creating pipeline object for independent features imputation
        try:
            logging.info("Creating KNN imputer pipeline")
            imputer=KNNImputer(**self.__config.imputer_config)
            preprocessor=Pipeline([("imputer",imputer)])
            logging.info("Created KNN imputer pipeline")
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_dataTransformation(self,train_filepath:str,test_filepath:str)->Tuple[str,str]:
        ##### This method is responsible for peforming data transformation
        try:
            logging.info("starting data transformation")
            train_df=read_csv(train_filepath)
            test_df=read_csv(test_filepath)
            os.makedirs(self.__config.trasformer_filedir,exist_ok=True)

            x_train=train_df.drop(columns=[self.__config.target_column],axis=1)
            y_train=train_df[self.__config.target_column]
            y_train.replace(-1,0,inplace=True)

            x_test=test_df.drop(columns=[self.__config.target_column],axis=1)
            y_test=test_df[self.__config.target_column]
            y_test.replace(-1,0,inplace=True)

            preprocessor=self.get_transformer();
            x_train_imputed=preprocessor.fit_transform(x_train)
            x_test_imputed=preprocessor.transform(x_test)

            logging.info("data transformation completed")
            
            train_data=np.c_[x_train_imputed,y_train]
            test_data=np.c_[x_test_imputed,y_test]
            logging.info("Saving transformed test and train data and transformer model")
            os.makedirs(self.__config.transformed_dir,exist_ok=True)
            save_numpyArray_data(filepath=self.__config.transformed_train_filepath,data=train_data)
            save_numpyArray_data(filepath=self.__config.transformed_test_filepath,data=test_data)
            save_pickle_file(filepath=self.__config.trasformer_filepath,data=preprocessor)
            logging.info("Transformed test and train data and transformer model saved")
            return (
                self.__config.transformed_train_filepath,
                self.__config.transformed_test_filepath
            )
        except Exception as e:
            raise CustomException(e,sys)
