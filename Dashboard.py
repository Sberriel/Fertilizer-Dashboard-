import streamlit as st 
import pandas as pd

st.write ("Fertilizers Dashboard")

df = pd.read_csv("FAOSTAT_11.csv")