import streamlit as st
import pandas as pd

st.title("🤖Machine Learning App")

st.info("Basic tutorial for learning streamlit with machine learning")

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
df
