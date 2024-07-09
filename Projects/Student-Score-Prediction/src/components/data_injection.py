import sys
import os
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from src.components.data_transformer import DataTransformer
from src.components.model_trainer import ModelTrainer

@dataclass
class DataInjectionConfig:
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')


class DataInjection:
    def __init__(self):
        self.config = DataInjectionConfig()

    def initialize(self):
        logging.info('Data Injection initialized')

        try:
            df = pd.read_csv('src/notebook/data/StudentsPerformance.csv')

            logging.info("Reading dataset from source")

            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            df.to_csv(self.config.raw_data_path, index=False, header=True)

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info("Data Injection completed")

            return (
                # self.config.raw_data_path,
                self.config.train_data_path,
                self.config.test_data_path
            )
            

        except Exception as e:
            logging.error(f'Error in Data Injection: {str(e)}')
            raise CustomException(f'Error in Data Injection: {str(e)}',sys)
        

if __name__ == '__main__':
    data_injection = DataInjection()
    X_train, X_test = data_injection.initialize()
    data_transformer = DataTransformer()
    X_train_arr, X_test_arr,_ = data_transformer.initialize_data_transmission(X_train, X_test)
    model_trainer = ModelTrainer()
    model_trainer.initialize_model_training(X_train_arr, X_test_arr)
