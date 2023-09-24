import sys
from source.mlproject.logger import logging
from source.mlproject.exception import CustomException
from source.mlproject.components.data_ingestion import DataIngestion
from source.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from source.mlproject.components.model_trainer import ModelTrainerConfig,ModelTrainer


if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        data_transformation=DataTransformation()
        train_array,test_array,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
        # Model Training
        
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array,test_array))
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    
    