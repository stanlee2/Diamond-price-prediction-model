import streamlit as st
import joblib
import numpy as np

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

def float_input_no_step(label, default="0.0"):
    val = st.sidebar.text_input(label, default)
    try:
        fval = float(val)
        st.sidebar.write(f"Value: {fval:.2f}")  # show formatted float
        return fval
    except ValueError:
        st.sidebar.error(f"Please enter a valid number for {label}")
        return 0.0

def int_input_no_step(label, default="1", min_val=1, max_val=10):
    val = st.sidebar.text_input(label, default)
    try:
        ival = int(val)
        if min_val <= ival <= max_val:
            st.sidebar.write(f"Value: {ival}")  # show int value
            return ival
        else:
            st.sidebar.error(f"Enter an integer between {min_val} and {max_val} for {label}")
            return min_val
    except ValueError:
        st.sidebar.error(f"Please enter a valid integer for {label}")
        return min_val

carat = float_input_no_step("Carat Weight", "0.00")
cut = int_input_no_step("Cut Quality", "1", 1, 10)
color = int_input_no_step("Color", "1", 1, 10)
clarity = int_input_no_step("Clarity", "1", 1, 10)
depth = float_input_no_step("Depth (%)", "0.00")
table = float_input_no_step("Table (%)", "0.00")
x = float_input_no_step("X Dimension (mm)", "0.00")
y = float_input_no_step("Y Dimension (mm)", "0.00")
z = float_input_no_step("Z Dimension (mm)", "0.00")

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