import streamlit as st

# Title
st.title("My First Streamlit App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("Hello, World!")

# Markdown
st.markdown("## Markdown Title")
st.markdown("### Markdown Subtitle")

# Displaying Data
import pandas as pd
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [30, 25, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
})
st.write("DataFrame:")
st.write(df)

# Widgets
number = st.slider("Select a number", 0, 100, 50)
st.write("You selected:", number)

if st.button("Say Hello"):
    st.write("Hello!")

option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

