import os;
import logging;
from datetime import datetime;


##### This code is responsible for creating log directories if not exist and log file for each execution with overridden basic config
try:
    LOG_PATH=os.path.join(os.getcwd(),"logs",datetime.now().strftime('%Y%m%d'))
    os.makedirs(LOG_PATH,exist_ok=True)

    timestmp=datetime.now().strftime('%Y%m%d_%H%M%S')
    LOG_FILENAME=f'netsec_{timestmp}.log'
    LOG_FILE_PATH=os.path.join(LOG_PATH,LOG_FILENAME)
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s',
        level=logging.INFO
    )

except Exception as e:
    print(f"Error occured while intializing the logger, error : {e}")
