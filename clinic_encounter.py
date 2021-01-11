import streamlit as st
import numpy as np
import pandas as pd

"""
# SAMC FM Residency Clinic Encounters
Requirements:
- 1650 in person FMP clinic encounters (FMP sites, nursing home, home visits)
- 165 encounters age < 10 y/o
- 165 encounters age > 60 y/o

Please upload raw data file in CSV
"""
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
    df['cln enc date'] = pd.to_datetime(df['cln enc date'])
    df['cln enc date'] = df['cln enc date'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    prvd_list = df['prvdr'].unique()
    sorted_provd = np.sort(prvd_list, axis = None)
    option = st.selectbox(
    'Please select a name', sorted_provd)
    
    res_name = df.loc[df['prvdr']== option]
    st.write ('**Provider:**', res_name.iloc[0]['prvdr'])
    st.write ('**Encounter Dates:**', res_name['cln enc date'].min(), 'to', res_name['cln enc date'].max(), '\n')
    st.write ('**Total Encounters:**', res_name['prvdr'].count())
    st.write ('**Age Groups (QTY)**')
    st.write ('Age < 10:', res_name.loc[res_name['patient age'] <= 10 , 'patient age'].count())
    st.write ('Age > 60:', res_name.loc[res_name['patient age'] >= 60 , 'patient age'].count())
    st.write ('**Sex (Percentage):**')
    st.dataframe((res_name['patientsex'].value_counts(normalize=True) * 100).round().astype(int))
    st.write ('**Race Group (Percentage)**')
    st.dataframe((res_name['race'].value_counts(normalize=True) * 100).round().astype(int))