import streamlit as st

st.header("First App")
name = st.text_input("Name")
age = st.number_input("Age")
st.write("Name:", name)
st.write("Age:", age)

st.subheader("Python Code")
st.code("import streamlit as st \nprint('Hello world') ")