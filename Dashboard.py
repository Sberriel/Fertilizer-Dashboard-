import streamlit as st 
import pandas as pd

df = pd.read_csv('FAOSTAT.csv')

st.markdown("Fertilizers Dashboard")


st.markdown(
    """
    <style>
    .custom-title {
        font-size: 85px;             /* Large font size */
        color: #0FA3B1;              /* Greenish-blue color */
        font-family: "Trebuchet MS", sans-serif;  /* Trebuchet MS font */
        text-align: left;            /* Left-aligned text */
    }
    </style>
    """,
    unsafe_allow_html=True
)