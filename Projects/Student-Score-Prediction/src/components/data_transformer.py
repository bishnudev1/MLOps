import os
import sys
from dataclasses import dataclass
import numpy as np
from sklearn.impute import SimpleImputer
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils import save_object


@dataclass
class DataTransformerConfig:
    preprocessor_object_file_path: str = os.path.join('artifacts', 'preprocessor_object.pkl')


class DataTransformer:
    def __init__(self):
        self.data_transformer_config = DataTransformerConfig()

    def get_transformation_object(self):
        try:
            numerical_columns = ['reading score', 'writing score']
            categorical_columns = ["gender","race/ethnicity","parental level of education","lunch","test preparation course"]

            numerical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])

            categorical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                # ('scaler', StandardScaler()),
                ('onehot', OneHotEncoder())
            ])

            logging.info("Neumerical Pipeline created")
            logging.info("Categorical Pipeline created")

            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', numerical_pipeline, numerical_columns),
                    ('cat', categorical_pipeline, categorical_columns)
                ])
            
            logging.info("Preprocessor created")

            return preprocessor

        except Exception as e:
            logging.error(f'Error in Data Transformation: {str(e)}')
            raise CustomException(f'Error in Data Transformation: {str(e)}', sys)
        
    def initialize_data_transmission(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # print(train_df.head())

            logging.info("Reading dataset from source")

            preprocessor = self.get_transformation_object()

            logging.info("Preprocessor created")

            target_column_name = 'math score'
            numerical_columns = ['reading score', 'writing score']

            input_train_feature_df = train_df.drop(columns=[target_column_name], axis=1)
            input_train_target_df = train_df[target_column_name]

            input_test_feature_df = test_df.drop(columns=[target_column_name], axis=1)
            input_test_target_df = test_df[target_column_name]

            # print(input_train_feature_df.head())

            logging.info("Data split into features and target")

            input_train_feature_df_scaled = preprocessor.fit_transform(input_train_feature_df)
            input_test_feature_df_scaled = preprocessor.transform(input_test_feature_df)

            # train_arr = np.c_(input_train_feature_df_scaled, np.array(input_train_target_df))

            # test_arr = np.c_(input_test_feature_df_scaled, np.array(input_test_target_df))

            train_arr = np.concatenate((input_train_feature_df_scaled, np.array(input_train_target_df).reshape(-1,1)), axis=1)
            test_arr = np.concatenate((input_test_feature_df_scaled, np.array(input_test_target_df).reshape(-1,1)), axis=1)

            logging.info("Data transformed and scaled")

            save_object(
                file_path=self.data_transformer_config.preprocessor_object_file_path,
                obj = preprocessor
            )

            return (
                train_arr,
                test_arr,
                preprocessor
            )


        except Exception as e:
            logging.error(f'Error in Data Transformation: {str(e)}')
            raise CustomException(f'Error in Data Transformation: {str(e)}', sys)