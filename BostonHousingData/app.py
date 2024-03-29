import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Loading Model
model = pickle.load(open("BostonHousingModel.sav", "rb"))

# Preparing Data
input_data = np.asarray([[-0.43942006,  3.12628155, -1.12165014, -0.27288841, -1.42262747,
        -0.23979304, -1.31238772,  2.61111401, -1.0016859 , -0.5778192 ,
        -0.97491834,  0.41164221, -0.86091034]])

# Predicting Result
predictions = model.predict(input_data)
print("Predictions : ", predictions)