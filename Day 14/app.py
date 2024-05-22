import streamlit as st
from pycaret.classification import setup, compare_models, pull, save_model, load_model
import pandas as pd

from streamlit_pandas_profiling import st_profile_report
import ydata_profiling
import os

if os.path.exists ('./Day 14 Students files/dataset.csv'):
    df=pd.read_csv('dataset.csv', index_col=None)

with st.slider:
    st.image('https://cdn0.iconfinder.com/data/icons/machine-learning-flat/60/021_Decision_Making-1024.png')
    st.title('AutoML Classification')
    choice=st.radio("Navigation", ['Upload', 'EDA', 'Modelling', 'Download'])

if choice == 'Upload':
    st.title('Upload Your Data')
    file=st.file_uploader('Upload your dataset')
    if file:
        df=pd.read_csv(file, index_col=None)
        df.to_csv('dataset.csv', index=None)
        st.dataframe(df.head())

if choice == 'EDA':
    st.title ('Exploratory Data Analysis')