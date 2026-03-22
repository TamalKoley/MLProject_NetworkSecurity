import sys;
import os;
from dotenv import load_dotenv;
from logger.logger import logging;
from exception.exceptionhandler import CustomException;


if __name__=='__main__':
    try:
        pass
    except CustomException as e:
        logging.info(e)
