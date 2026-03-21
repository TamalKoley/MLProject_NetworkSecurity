import sys;
from logger.logger import logging;
from exception.exceptionhandler import CustomException;

if __name__=='__main__':
    try:
        logging.info("Program Started")
        a=1/0;
    except Exception as e:
        try:
            raise CustomException(e,sys)
        except Exception as err:
            logging.info(err)