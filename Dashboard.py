import streamlit as st 
import pandas as pd

df = pd.read_csv('FAOSTAT_11.csv')

st.write ("Fertilizers Dashboard")

st.markdown(
    """
    <style>
    .custom-title {
        font-size: 120px;       
        color: ##0FA3B1;        
        font-family: Trebichet MS, sans-serif; 
        text-align: left;     
    }
    </style>
    """,
    unsafe_allow_html=True
)