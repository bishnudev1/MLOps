from sklearn.linear_model import LinearRegression, LogisticRegression,LassoCV
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import AdaBoostRegressor
from xgboost import XGBRegressor
# from catboost import CatBoostRegressor
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from src.utils import evaluate_models
import os
import sys
from src.utils import save_object
import warnings


@dataclass
class ModelTrainerConfig:
    model_object_path:str = os.path.join('artifacts', 'model_object.pkl')


class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initialize_model_training(self,train_array, test_array):

        try:
            warnings.filterwarnings("ignore")
            logging.info('Model Trainer is initializing...')
            print('Model Trainer is initializing...')

            X_train, y_train, X_test, y_test = (
            train_array[:, :-1],
            train_array[:, -1],
            test_array[:, :-1],
            test_array[:, -1]
            )

            models = {
                'Linear Regression': LinearRegression(),
                'Logistic Regression': LogisticRegression(),
                'Random Forest Regressor': RandomForestRegressor(),
                # 'Gradient Boosting Regressor': GradientBoostingRegressor(),
                'Decision Tree Regressor': DecisionTreeRegressor(),
                'Support Vector Regressor': SVR(),
                'XGBoost Regressor': XGBRegressor(),
                'LassoCV': LassoCV(),
                'AdaBoost Regressor': AdaBoostRegressor(),
                'Gradient Boosting Regressor': GradientBoostingRegressor(),
            }

            logging.info(f'Model Training started')

            params = {
    'Linear Regression': {},
    'Logistic Regression': {
        'penalty': ['l1', 'l2', 'elasticnet'],
        'C': [0.1, 1, 10, 100, 1000],
        'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    },
    'Random Forest Regressor': {
        'n_estimators': [100, 200, 300, 400, 500],
        'max_depth': [10, 20, 30, 40, 50],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'bootstrap': [True, False],
    },
    'Decision Tree Regressor': {
        'max_depth': [10, 20, 30, 40, 50],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['auto', 'sqrt', 'log2'],
    },
    'Support Vector Regressor': {
        'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
        'C': [0.1, 1, 10, 100, 1000],
        'gamma': ['scale', 'auto'],
    },
    'XGBoost Regressor': {
        'n_estimators': [100, 200, 300, 400, 500],
        'learning_rate': [0.01, 0.1, 1],
        'subsample': [0.5, 0.7, 1.0],
        'max_depth': [3, 7, 9],
    },
    'LassoCV': {
        'alphas': [[0.1, 1, 10, 100, 1000]],
    },
    'AdaBoost Regressor': {
        'n_estimators': [100, 200, 300, 400, 500],
        'learning_rate': [0.01, 0.1, 1],
    },
    'Gradient Boosting Regressor': {
        'n_estimators': [100, 200, 300, 400, 500],
        'learning_rate': [0.01, 0.1, 1],
        'subsample': [0.5, 0.7, 1.0],
        'max_depth': [3, 7, 9],
    },
        }


            report = evaluate_models(models,params, X_train, y_train, X_test, y_test)

            logging.info(f'Model Training completed')

            best_model_score = max(sorted(report.values(), reverse=True))

            best_model_name = list(report.keys())[list(report.values()).index(best_model_score)]

            if best_model_score < 0.6:
                logging.error(f'Best Model: {best_model_name} with R2 Score: {best_model_score} with low accuracy < 0.6') 
                raise CustomException(f'Best Model: {best_model_name} with R2 Score: {best_model_score} with low accuracy < 0.6', sys)

            logging.info(f'Best Model: {best_model_name} with R2 Score: {best_model_score}')

            save_object(self.config.model_object_path, models[best_model_name])

            return (
                best_model_name,
                best_model_score
            )
        
        except Exception as e:
            logging.error(f'Error in Model Training: {str(e)}')
            raise CustomException(f'Error in Model Training: {str(e)}', sys)