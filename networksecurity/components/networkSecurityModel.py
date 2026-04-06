import os,sys;

from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.logger.logger import logging;

class NetworkSecurityModel:
    #### This class is responsible for transforming input and making prediction
    def __init__(self,model,preprocessor):
        ### constructor
        try:
            self.__model=model;
            self.__preprocessor=preprocessor;
        except Exception as e:
            raise CustomException (e,sys)
        
    def predict(self,x):
        #### this function is responsible for transforming input and making prediction
        try:
            logging.info("transforimg input and making predictions")
            x_transformed=self.__preprocessor.transform(x)
            y_pred=self.__model.predict(x_transformed)
            logging.info("Prediction completed")
            return y_pred;
        except Exception as e:
            raise CustomException(e,sys);

        