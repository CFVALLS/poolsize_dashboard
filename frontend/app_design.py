#################################################################
###################         Libraries        ####################
#################################################################

import streamlit as st
from sample_calculation import dict_streamlit_output
from numpy import random
import matplotlib.pyplot as plt
import SessionState
import scipy.stats

#########################################################
################### WEBSITE DESIGN ######################
#########################################################


st.set_page_config(layout="wide")

######################## TITLE ##########################

col1, col2 = st.columns((2, 1))

with col1:
    new_title = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30; font-size:3rem;">POOL-SIZE IMPACT ON <p style="font-family:sans-serif; font-weight: bold; color:Red; font-size:5rem;">qPCR </p> <p style="font-family:sans-serif; font-weight: bold; color:#050a30; font-size:3rem;"> WORKFLOW</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    #st.title("Pool-Size impact on qPCR Workflow")

with col2:
    col2_text = '<p style="font-family:sans-serif; font-weight: bold; text-align: right; vertical-align: text-bottom; color:Blue; font-size:1rem;"> <a href="https://github.com/CFVALLS">Author: Cristian Valls </a></p>'
    st.markdown(col2_text, unsafe_allow_html=True)
    #st.title("Pool-Size impact on qPCR Workflow")

######################## BODY ##########################

col3, col4 = st.columns((1, 2))

with col3:
    text1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:2rem; margin-top: 2rem; "> Rationale</p>'
    st.markdown(text1, unsafe_allow_html=True)
    text1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem;margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">RT-PCR is the gold-standard laboratory technique for identifying SARS-CoV-2 in a clinical setting. However, the high demand for this technique produced a deficit in the supply chain of different reactive required to perform qPCR. One method to maximize the reagents for qPCR is by ‘Pooling samples’. This has been used in other screening protocols and has also been proposed for the detection of SARS-CoV-2. </p>'
    st.markdown(text1, unsafe_allow_html=True)
    text2 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> Sample pooling is the method by which multiple specimens are extracted using one RNA isolation kit and then processed as a single PCR test without significant loss of sensitivity.</p>'
    st.markdown(text2, unsafe_allow_html=True)
    text3 = '<p style="font-family:sans-serif; font-weight: bold; color:Red ;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">  This Streamlit App shows how many pools per sample are ideal to maximize reagents in a one-stage pool strategy (i.e., pool samples, if positive, run samples individually) </p>'
    st.markdown(text3, unsafe_allow_html=True)
    text4 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:2rem; margin-top: 1rem; "> References</p>'
    st.markdown(text4, unsafe_allow_html=True)

    reference_1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30; ;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">  2021 Apr 17;21(1):360. doi: 10.1186/s12879-021-06061-3.</p>'
    st.markdown(reference_1, unsafe_allow_html=True)


with col4:
    text2 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1.8rem;margin-top: 1.8rem; text-align: center; "> Choose Population size screened and positivity</p>'
    st.markdown(text2, unsafe_allow_html=True)
    label_3 = "Positivity Rate"
    POSITIVITY = st.slider(label_3, min_value=1.0,
                           max_value=25.0, value=5.0, step=0.2)
    label_4 = 'Number of samples'
    NUM_SAMPLES = st.slider(label_4, min_value=1,
                           max_value=100000, value=5000, step=10)

    str_input_summary = '<h2 style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1.5rem;margin-top: 1rem; text-align: center;"> Input values to simulate  </h2> '
    st.markdown(str_input_summary, unsafe_allow_html=True)


col5, col6 = st.columns((1, 1))

with col5:
    text2 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:2rem;margin-top: 2rem; "> How it Works:</p>'
    st.markdown(text2, unsafe_allow_html=True)
    text1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> We generate a population with a predefined number of positive cases. Population Size (number of samples), Positivity (positive rate for SARS-CoV-2 detection) and Pool-size(number of samples per pool) are defined by the user. according to the positivity that is inputted by users. Then a population is randomly generated with the positivity defined. </p>'
    st.markdown(text1, unsafe_allow_html=True)
    text2 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> FIRST: select - Population Size (number of samples), Positivity (positive rate for SARS-CoV-2 detection) and Pool-size(number of samples per pool). according to the positivity that is inputted by users. Then a population is randomly generated with the positivity defined. </p>'
    st.markdown(text2, unsafe_allow_html=True)
    text3 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> SECOND: According to the positivity that is inputted by users, a population is randomly generated. Then a population is randomly generated with the positivity defined. </p>'
    st.markdown(text3, unsafe_allow_html=True)
    text4 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> THIRD: Using the population generated, we pool samples by the size determined by the user </p>'
    st.markdown(text4, unsafe_allow_html=True)
    text5 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> FOURTH: Pools are analyzed; if it contains a positive sample , that pool is proccesed as individually</p>'
    st.markdown(text5, unsafe_allow_html=True)
    text6 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> COUNT: we count every pool created and every individual reaction derived from a positive pool and register the number of total theoric reactions performed. This process is repeated 250 times, and a frecuency histogram is plotted</p>'
    st.markdown(text6, unsafe_allow_html=True)
