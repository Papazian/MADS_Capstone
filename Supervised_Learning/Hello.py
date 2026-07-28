import streamlit as st

# 1. Set up the page title
st.title("My First Streamlit App")

# 2. Add a simple text input widget
user_name = st.text_input("Enter your name:", "Guest")

# 3. Add a slider widget
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)

# 4. Add a button to trigger an action
if st.button("Greet Me"):
    # Display the result using st.write
    st.write(f"Hello, {user_name}! You are {age} years old.")