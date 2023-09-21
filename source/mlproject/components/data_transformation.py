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
from source.mlproject.utils import save_object

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
                ('One_Hot_Encoder',OneHotEncoder()),
                ('Scalar',StandardScaler(with_mean=False))
            ])
            
            logging.info(f"Categorical Columns:{categorical_columns}")
            logging.info(f"Numerical Columns:{numerical_columns}")
            
            
            preprocessor=ColumnTransformer(
                [
                    ('Num_Pipeline',numerical_pipeline,numerical_columns),
                    ('Cat_Pipeline',categorical_pipeline,categorical_columns)
                ]
            )
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info('Reading the train & test files')
            
            preprocessing_object=self.get_data_transformer_object()
            
            target_column_name='math_score'
           
            
            #Divide The Train Dataset into Independent & Dependent Feature
            input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]
            
            
            #Divide The Test Dataset into Independent & Dependent Feature
            input_features_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            
            logging.info('Applying Preprocessing on Traning & Test Dataframe')
            
            input_features_train_arr=preprocessing_object.fit_transform(input_features_train_df)
            input_features_test_arr=preprocessing_object.transform(input_features_test_df)
            
            train_array=np.c_[input_features_train_arr,np.array(target_feature_train_df)]
            test_array=np.c_[input_features_test_arr,np.array(target_feature_test_df)]
            
            logging.info('Saved Preprocessing Object')
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                object=preprocessing_object
            )
            
            return(
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_obj_file_path
                
            )

        except Exception as e:
            raise CustomException(e,sys)