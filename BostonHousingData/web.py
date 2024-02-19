# To Run a Model on WEB
import numpy as np
import streamlit as st
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

# Loading Model
model = pickle.load(open("BostonHousingModel.sav", 'rb'))
# Loading Model
my_pipeline = pickle.load(open("pipeline.sav", 'rb'))

# Function for Prediction
def price_prediction(input_data):
    # Converting input_data to numpy Array
    input = np.asarray(input_data)
    # Reshaping the array COnverting array t 2-D Array
    input = input.reshape(1, -1)
    # Saving The Predictions in Variable
    predictions = model.predict(input)

    return predictions


st.title("Boston Housing Data Price Prediction")
# Getting Input Data From User
Input = []
CRIM = st.number_input("Enter Crime Rate(per capita crime rate by town) : ")
Input.append(CRIM)
ZN = st.number_input("Proportion of residential land zoned for lots over 25,000 sq.ft")
Input.append(ZN)
INDUS = st.number_input("Proportion of non-retail business acres per town")
Input.append(INDUS)
CHAS = st.number_input("Charles River dummy variable")
Input.append(CHAS)
NOX = st.number_input("Nitric oxides concentration (parts per 10 million)")
Input.append(NOX)
RM = st.number_input("Average number of rooms per dwelling")
Input.append(RM)
AGE = st.number_input("Proportion of owner-occupied units built prior to 1940")
Input.append(AGE)
DIS = st.number_input("weighted distances to five Boston employment centres")
Input.append(DIS)
RAD = st.number_input("Index of accessibility to radial highways")
Input.append(RAD)
TAX = st.number_input("Full-value property-tax rate per $10,000")
Input.append(TAX)
PTRATIO = st.number_input("Pupil-teacher ratio by town")
Input.append(PTRATIO)
B = st.number_input("1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town")
Input.append(B)
LSTAT = st.number_input('''% lower status of the population''')
Input.append(LSTAT)

Input = np.asarray(Input)
Input = Input.reshape(1, -1)  

# Transforming Required Data
Input = my_pipeline.transform(Input)

# Creating Button
if st.button("Predict"):
    predictions = price_prediction(Input)
    st.write("Predicted Price For The Property is ", predictions[0] * 1000,"$ 's" )