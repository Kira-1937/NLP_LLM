import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Title
st.title("Advanced Streamlit App")

# Authentication
def authenticate(username, password):
    # Replace with your authentication logic
    if username == "admin" and password == "password":
        return True
    else:
        return False

username = st.text_input("Username:")
password = st.text_input("Password:", type="password")

if st.button("Login"):
    if authenticate(username, password):
        st.success("Logged in successfully!")
    else:
        st.error("Authentication failed. Please try again.")

# Load data
@st.cache
def load_data():
    return pd.DataFrame({
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [30, 25, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']
    })

df = load_data()

# Display DataFrame
st.write("## DataFrame:")
st.write(df)

# Interactive Plot
st.write("## Interactive Plot")
plot_type = st.selectbox("Select plot type", ["Line Plot", "Bar Plot"])
if plot_type == "Line Plot":
    st.line_chart(df['Age'])
elif plot_type == "Bar Plot":
    st.bar_chart(df['Age'])

# Custom Component
st.write("## Custom Component")

# Custom Button
def custom_button(text):
    return f"<button>{text}</button>"

button_text = st.text_input("Enter button text:")
if st.button("Display Button"):
    button_html = custom_button(button_text)
    st.write(button_html, unsafe_allow_html=True)

# Markdown
st.markdown("## Markdown Title")
st.markdown("### Markdown Subtitle")
