import numpy as np
import pandas as pd
import pickle
from src.exception import CustomException
from src.logger import logging
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV


def load_object(file_path):
    try:
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    except Exception as e:
        raise CustomException(f'Error in loading object: {str(e)}')


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise CustomException(f'Error in saving object: {str(e)}')


def evaluate_models(models, params, X_train, y_train, X_test, y_test):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            # model.fit(X_train, y_train)
            logging.info("Hyperparameter tuning has started")
            grid = GridSearchCV(model, param, n_jobs=-1, cv=3)
            grid.fit(X_train, y_train)
            model.set_params(**grid.best_params_)
            model.fit(X_train, y_train)
            logging.info("Hyperparameter tuning has completed")
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            report[list(models)[i]] = r2
            print(f'{list(models)[i]}: mse={mse}, mae={mae}, r2={r2}')
        return report
 
    except Exception as e:
        raise CustomException(f'Error in evaluating models: {str(e)}')