import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
#import pickle
import joblib 
from joblib import Parallel, delayed


df = pd.read_csv('https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv', index_col=False)

st.title('Student Score Prediction')

st.sidebar.write('Predicition is based on below dataset')
st.sidebar.dataframe(df)

st.markdown("Know your score based on study hours!")
hours = st.number_input('Enter your daily average study hours')

#new_model = joblib.load("score_prediction.pkl")
new_model = joblib.load("score_prediction.pkl") 

button = st.button("Predict")

if hours>9.89:
    st.subheader("Invalid data!!")

else:
    if button:

        predicted = new_model.predict([[hours]])
        score = predicted.item()
        st.subheader(f"You might score : {score}")

