import streamlit as st
import joblib
import numpy as np
from PIL import Image
import os

# Set the page configuration
st.set_page_config(page_title="Diamond Gemstone Price Prediction", page_icon="💎", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .reportview-container {
        background-color: #f4f7f6;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2980b9;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    h1 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("💎 Diamond Gemstone Price Prediction")
st.subheader("⬅️ Enter diamond features at the side pane widgets to estimate its market value")

# Load image if available
image_path = "diamond_image.jpg"  # Replace with your actual image path or name
if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, use_column_width=True)

# Sidebar input section
st.sidebar.header("Input Diamond Parameters")

carat = st.sidebar.number_input("Carat Weight", min_value=0.0, value=0.0, step=0.01, format="%.2f")
cut = st.sidebar.number_input("Cut Quality", min_value=1, max_value=10, value=1, step=1)
color = st.sidebar.number_input("Color", min_value=1, max_value=10, value=1, step=1)
clarity = st.sidebar.number_input("Clarity", min_value=1, max_value=10, value=1, step=1)
depth = st.sidebar.number_input("Depth (%)", min_value=0.0, value=0.0, step=0.1, format="%.2f")
table = st.sidebar.number_input("Table (%)", min_value=0.0, value=0.0, step=0.1, format="%.2f")
x = st.sidebar.number_input("X Dimension (mm)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
y = st.sidebar.number_input("Y Dimension (mm)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
z = st.sidebar.number_input("Z Dimension (mm)", min_value=0.0, value=0.0, step=0.01, format="%.2f")

# Load the model
try:
    model = joblib.load("model_joblib.pkl")
except FileNotFoundError:
    st.error("Model file 'model_joblib.pkl' not found. Please check the file path.")
    st.stop()

# Predict button
if st.button("Predict Price"):
    input_data = np.array([carat, cut, color, clarity, depth, table, x, y, z]).reshape(1, -1)
    prediction = model.predict(input_data)
    st.markdown(f"""
    <h3 style='color: #2ecc71;'>💰 Estimated Price: ${prediction[0]:,.2f}</h3>
    """, unsafe_allow_html=True)