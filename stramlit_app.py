import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

#text
st.title("Hell app")
st.header("Hello Header")
st.subheader("Hello sub header")

if st.sidebar.checkbox("Show data"):
    df


var=st.sidebar.number_input("Enter number :- ")
st.subheader(var)

st.video("https://youtu.be/fyTOcD1J9js", format="video/mp4", start_time=0)
