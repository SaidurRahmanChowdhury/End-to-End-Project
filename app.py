import sys
from source.mlproject.logger import logging
from source.mlproject.exception import CustomException
from source.mlproject.components.data_ingestion import DataIngestion

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)