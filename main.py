import numpy as np
import pandas as pd
import streamlit as st 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('# EDA Automation')

with st.sidebar.header('1. Upload your CSV File'):
    uploaded_file = st.sidebar.file_uploader('Upload your CSV file', type=['csv'])
    st.sidebar.markdown('''
    [Example CSV File](https://raw.githubusercontent.com/crinex/EDA-Automation/master/)
    ''')