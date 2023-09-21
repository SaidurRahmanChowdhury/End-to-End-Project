import sys
from source.mlproject.logger import logging
from source.mlproject.exception import CustomException
from source.mlproject.components.data_ingestion import DataIngestion
from source.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation


if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
    