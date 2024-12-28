import streamlit as st
import pandas as pd


df = pd.read_csv("FAOSTAT.csv")


st.title("Fertilizers Dashboard")


st.title(
    """
    <style>
    .custom-title {
        font-size: 85px;  /* Large font size */
        color: #0FA3B1;   /* Green-blue color */
        font-family: "Trebuchet MS", sans-serif;
        text-align: left; /* Left alignment */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<h1 class="custom-title">Fertilizers Dashboard</h1>', unsafe_allow_html=True)


