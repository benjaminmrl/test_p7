import datetime
import requests

import streamlit as st
import numpy as np
import streamlit.components.v1 as components
#from lime.lime_tabular import LimeTabularExplainer

#Onglet
tab1,tab2 = st.tabs(["Donnees client","Explain"])
with tab1:
    #st.image('PAD.png')
    tab1.subheader("Client")
    add_selectbox1 = st.selectbox(
        'Genre',
     ('Mr', 'Mme', 'Autre'))  
    title = st.text_input('Nom', 'Nom')
    title = st.text_input('Prenom', 'Prenom')
    title = st.text_input('Adresse', 'Adresse')
    title = st.text_input('CP', 'Code Postal')
    title = st.text_input('Ville', 'Ville')
    date_naissance = st.date_input("Date de naissance",
                                   datetime.date(2001, 11, 9))

    data1 = st.number_input('CREDIT_TO_ANNUITY_RATIO', value=0.416986)
    data2 = st.number_input('EXT_SOURCE_1', value=0.0)
    data3 = st.number_input('EXT_SOURCE_2', value=-0.38)
    data4 = st.number_input('EXT_SOURCE_3', value=0.0)
    data5 = st.number_input('DAYS_BIRTH', value=-0.689503)
    data6 = st.number_input('AMT_ANNUITY', value=0.128735)
    data7 = st.number_input('MEDIAN(payments.AMT_PAYMENT)', value=-0.465475)
    data8 = st.number_input('AMT_GOODS_PRICE', value=0.510204)
    data9 = st.number_input('DAYS_ID_PUBLISH', value=-0.353238)
    data10 = st.number_input('COUNT(bureau)', value=0.166667)
    data11 = st.number_input('COUNT(cash_balance)', value=-0.037037)
    data12 = st.number_input('MEDIAN(cash_balance.CNT_INSTALMENT_FUTURE)', value=0.444444)
    data13 = st.number_input('AMT_CREDIT', value=0.299766)
    data14 = st.number_input('MEDIAN(prev_app.CNT_PAYMENT)', value=0.0)
    data15 = st.number_input('MEDIAN(bureau.DAYS_CREDIT_ENDDATE)', value=-1.905672)
    data16 = st.number_input('CODE_GENDER', value=1.0)
    data17 = st.number_input('DAYS_EMPLOYED', value=-1.265463)
    data18 = st.number_input('MEDIAN(bureau.AMT_CREDIT_SUM)', value=-0.423168)
    data19 = st.number_input('MEDIAN(bureau.AMT_CREDIT_MAX_OVERDUE)', value=31.5)
    data20 = st.number_input('NAME_EDUCATION_TYPE', value=0.0)

with st.form("my_form"):
    st.write("Soumettre le dossier")
   
   # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        valeuratester = {
        'CREDIT_TO_ANNUITY_RATIO': data1,
        'EXT_SOURCE_1': data2,
        'EXT_SOURCE_2': data3,
        'EXT_SOURCE_3': data4,
        'DAYS_BIRTH': data5,
        'AMT_ANNUITY': data6,
        'MEDIAN(payments.AMT_PAYMENT)': data7,
        'AMT_GOODS_PRICE': data8,
        'DAYS_ID_PUBLISH': data9,
        'COUNT(bureau)': data10,
        'COUNT(cash_balance)': data11,
        'MEDIAN(cash_balance.CNT_INSTALMENT_FUTURE)': data12,
        'AMT_CREDIT': data13,
        'MEDIAN(prev_app.CNT_PAYMENT)': data14,
        'MEDIAN(bureau.DAYS_CREDIT_ENDDATE)': data15,
        'CODE_GENDER': data16,
        'DAYS_EMPLOYED': data17,
        'MEDIAN(bureau.AMT_CREDIT_SUM)': data18,
        'MEDIAN(bureau.AMT_CREDIT_MAX_OVERDUE)': data19,
        'NAME_EDUCATION_TYPE': data20,
        }
        r = requests.get('http://127.0.0.1:5002/solvabilite', json = valeuratester)
        solvable = r.json()
        print(solvable)
 
with tab2:
    st.image('../image/test.png')