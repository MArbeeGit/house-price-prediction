import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the feature names used during training
with open('feature_names.txt', 'r') as f:
    feature_names = f.read().split(',')

# Create input fields
st.title("House Price Prediction")
overall_qual = st.slider("Overall Quality (1-10)", min_value=1, max_value=10, value=5)
gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", min_value=0, max_value=10000, value=1500)
total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=10000, value=1000)
garage_cars = st.slider("Garage Capacity (cars)", min_value=0, max_value=5, value=2)
year_built = st.slider("Year Built", min_value=1800, max_value=2023, value=2000)

# Create a NumPy array with the same structure as X_train
input_data = np.array([[overall_qual, gr_liv_area, total_bsmt_sf, garage_cars, year_built]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ${prediction[0]:,.2f}")