import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.markdown('# EDA Automation')

with st.sidebar.header('Upload your CSV File'):
    uploaded_file = st.sidebar.file_uploader(
        'Upload your CSV file', type=['csv'])
    st.sidebar.markdown('''
    [Example CSV File](https://raw.githubusercontent.com/crinex/EDA-Automation/master/netflix_titles.csv)
    ''')

if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**INPUT DATAFRAME**')
    st.write(df)
    st.write('---')
    st.header('**PANDAS PROFILING REPORT**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
