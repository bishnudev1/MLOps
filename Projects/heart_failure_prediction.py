# -*- coding: utf-8 -*-
"""Heart Failure Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a6j1baAZKq0INOIOjuOwsuzaneI1YK7i
"""

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heart.csv')

df.head(1)

df.isnull().sum()

df["Sex"].value_counts()

df["HeartDisease"].value_counts()

df["ChestPainType"].value_counts()

df["RestingECG"].value_counts()

df["ExerciseAngina"].value_counts()

df["ST_Slope"].value_counts()

df.columns.str.strip()

from sklearn.preprocessing import LabelEncoder

l1 = LabelEncoder()

df["Sex"] = l1.fit_transform(df["Sex"])

l2 = LabelEncoder()

df["ExerciseAngina"] = l2.fit_transform(df["ExerciseAngina"])

import pickle

with open('l1r.pkl', 'wb') as file:
    pickle.dump(l1, file)

with open('l2r.pkl', 'wb') as file:
    pickle.dump(l2, file)

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

cat_features = X.select_dtypes(include="object").columns
num_features = X.select_dtypes(exclude="object").columns

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
scaler = StandardScaler()

transformer = ColumnTransformer(transformers=[
    ('ohe', ohe, cat_features),
    ('scaler', scaler, num_features)
], remainder='passthrough')

with open('transformer.pkl', 'wb') as file:
    pickle.dump(transformer, file)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

random_forest_params = {
    'n_estimators': [10, 20, 50, 100, 200],
    'max_depth': [None, 5, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(estimator=RandomForestClassifier(),
                           param_grid=random_forest_params,
                           cv=5,
                           n_jobs=-1,
                           verbose=1)

X_train_transformed = transformer.fit_transform(X_train)
X_test_transformed = transformer.transform(X_test)

grid_search.fit(X_train_transformed, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_}")

model = RandomForestClassifier()

model.set_params(**grid_search.best_params_)

pipe = Pipeline([
    ('transformer', transformer),
    ('model', model)
])

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)
y_pred

#showing dataframe of first 10 y_real y_pred and difference

pd.DataFrame({
    "y_real": y_test[:10],
    "y_pred": y_pred[:10],
    "difference": y_test[:10] - y_pred[:10]
})

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print(f"accuracy_score: {accuracy_score(y_test, y_pred)*100}%")
print(f"precision_score: {precision_score(y_test, y_pred)}")
print(f"recall_score: {recall_score(y_test, y_pred)}")

import pickle

with open('model.pkl', 'wb') as file:
    pickle.dump(pipe, file)

X.head(1)

test_data = pd.DataFrame({
    'Age': [63],
    'Sex': ['M'],
    'ChestPainType': ['ATA'],
    'RestingBP': [145],
    'Cholesterol': [23],
    'FastingBS': [1],
    'RestingECG': ['Normal'],
    'MaxHR': [140],
    'ExerciseAngina': ['N'],
    'Oldpeak': [1.2],
    'ST_Slope': ['Flat']
})

with open('l1r.pkl', 'rb') as file:
    l1 = pickle.load(file)

with open('l2r.pkl', 'rb') as file:
    l2 = pickle.load(file)

test_data["Sex"] = l1.transform(test_data["Sex"])
test_data["ExerciseAngina"] = l2.transform(test_data["ExerciseAngina"])

test_data

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

result = model.predict(test_data)


if result[0] == 1:
    print("The person has heart disease.")
else:
    print("The person does not have heart disease.")