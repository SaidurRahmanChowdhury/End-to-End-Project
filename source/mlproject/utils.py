import os
import sys
from source.mlproject.exception import CustomException
from source.mlproject.logger import logging
import pandas as pd
import pymysql
from dotenv import load_dotenv
import numpy as np
import pickle


load_dotenv()

host=os.getenv('host')
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')


def read_sql_data():
    logging.info('Reading Sql Database Started')
    try:
        # Connect to the database
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db   
        )
        logging.info("Connection Established: %s", mydb)
        df=pd.read_sql_query('select * from student',mydb)
        print(df.head())
        
        return df
        
    except Exception as ex:
        raise CustomException(ex)
 
    
def save_object(file_path,object):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
        
        with open(file_path,'wb') as file_object:
            pickle.dump(object,file_object)
            
    except Exception as e:
        raise CustomException(e,sys)