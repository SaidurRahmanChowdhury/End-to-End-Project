import sys
import os
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from source.mlproject.exception import CustomException
from source.mlproject.logger import logging


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')
    
class DataTransformation:
    
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    
    def get_data_transformer_object(self):
        
        try:
            numerical_columns=['writing_score','reading_score']
            categorical_columns=['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']
            
            numerical_pipeline=Pipeline(steps=[
                ('Imputer',SimpleImputer(strategy='median')),
                ('Scalar',StandardScaler())
            ])
            
            categorical_pipeline=Pipeline(steps=[
                ('Imputer',SimpleImputer(strategy='most_frequent')),
                ('Scalar',StandardScaler(with_mean=False))
            ])
            
            logging.info(f"Categorical Columns:{categorical_columns}")
            logging.info(f"Numerical Columns:{numerical_columns}")

        except Exception as e:
            raise CustomException(e,sys)
        