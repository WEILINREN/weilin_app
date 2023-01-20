import streamlit as st
import pandas as pd

st.title('My Data Analysis App')

data_url = st.text_input('Enter a URL to download a CSV file:')
if data_url:
    data = pd.read_csv(data_url)
    st.dataframe(data.head())

if st.checkbox('Show summary statistics'):
    st.write(data.describe())

chart_type = st.selectbox('Select a chart type', ['bar', 'line', 'histogram'])
if chart_type == 'bar':
    st.bar_chart(data)
elif chart_type == 'line':
    st.line_chart(data)
else:
    st.histogram(data)
