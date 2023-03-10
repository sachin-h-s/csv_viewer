import streamlit as st
import pandas as pd

st.title('CSV Viewer')

uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('Shape:', df.shape)
    st.table(df)
    

