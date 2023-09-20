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
            pass
        
        except Exception as e:
            raise CustomException(e,sys)
        