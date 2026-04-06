import sys;
import os;
# from dotenv import load_dotenv;
from networksecurity.logger.logger import logging;
from networksecurity.exception.exceptionhandler import CustomException;
from networksecurity.components.dataIngestion import DataIngestion;
from networksecurity.components.dataValidation import DataValidation;
from networksecurity.components.dataTransformation import DataTransformation;
from networksecurity.components.modelTraining import ModelTraining;
from networksecurity.utils.pickleFileUtil import load_pickle_file;


if __name__=='__main__':
    try:
        # logging.info('Main Program Started')
        # di=DataIngestion()
        # train_filepath,test_filepath=di.initiate_dataingestion();
        # dv=DataValidation()
        # dv.initiate_data_validation(test_filepath=test_filepath,train_filepath=train_filepath)
        # dt=DataTransformation();
        # trainNParray_path,testNParray_path=dt.initiate_dataTransformation(train_filepath=train_filepath,test_filepath=test_filepath)
        # trainer=ModelTraining()
        # trainer.initiate_model_training(train_datapath=trainNParray_path,test_datapath=testNParray_path)
        # logging.info('Main Program Completed')

        model=load_pickle_file(filepath='Final_Models/trained_model.pkl')
        y_pred=model.predict([[1,0,-1,1,1,-1,1,1,-1,1,1,-1,1,0,1,-1,1,1,0,1,1,1,1,1,-1,1,1,1,0,1]])
        print(f'prediction is {y_pred}')
    except CustomException as e:
        logging.info(e)
