import streamlit as st
import pickle
import tensorflow as tf
import pandas as pd


model = tf.keras.models.load_model('churn_model.h5')

with open('standard_scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('label_encoder.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

with open('onehot_encoder.pkl', 'rb') as file:
    one_hot_encoder = pickle.load(file)

st.title("Customer Churn Prediction")

# df = {
#     'CreditScore': 600,
#     'Geography': 'France',
#     'Gender': 'Male',
#     'Age': 40,
#     'Tenure': 3,
#     'Balance': 60000,
#     'NumOfProducts': 2,
#     'HasCrCard': 1,
#     'IsActiveMember': 1,
#     'EstimatedSalary': 50000
# }

credit_score = st.slider('Credit Score', 300, 850, 600)
geography = st.selectbox('Geography', one_hot_encoder.categories_[0])
gender = st.selectbox('Gender',label_encoder.classes_)
age = st.slider('Age', 18, 100, 40)
tenure = st.slider('Tenure', 0, 10, 3)
balance = st.slider('Balance', 0, 250000, 60000)
num_of_products = st.slider('Number of Products', 1, 4, 2)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])
estimated_salary = st.slider('Estimated Salary', 0, 250000, 50000)

data = {
    'CreditScore': credit_score,
    'Geography': geography,
    'Gender': gender,
    'Age': age,
    'Tenure': tenure,
    'Balance': balance,
    'NumOfProducts': num_of_products,
    'HasCrCard': has_cr_card,
    'IsActiveMember': is_active_member,
    'EstimatedSalary': estimated_salary
}

df = pd.DataFrame(data, index=[0])

df["Gender"] = label_encoder.transform(df["Gender"])[0]

dfg = pd.DataFrame(one_hot_encoder.transform(df[["Geography"]]).toarray(), columns=one_hot_encoder.get_feature_names_out(["Geography"]))

new_df = pd.concat([df.drop("Geography", axis=1), dfg], axis=1)

new_df = scaler.transform(new_df)

prediction = model.predict(new_df)

if prediction > 0.5:
    st.write("Customer will churn")
else:
    st.write("Customer will not churn")
