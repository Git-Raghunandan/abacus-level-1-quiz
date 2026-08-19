import streamlit as st

st.title("Abacus Level 1 Quiz")

st.write("Streamlit is working!")

name = st.text_input("Enter your name")

if st.button("Start"):
    st.success(f"Hello {name}!")
