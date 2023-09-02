import sys
from source.mlproject.logger import logging
from source.mlproject.exception import CustomException

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)