import streamlit as st
import pandas as pd

st.title("🤖Machine Learning APP!")
st.write('I am learning streamlit')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
df.head(2)
