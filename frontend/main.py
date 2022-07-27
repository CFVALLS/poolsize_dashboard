import streamlit as st
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import SessionState
import scipy.stats


################### CONFIGURATION ###########################

st.set_page_config(layout="wide")

################### CONSTANTS & Functions ###############################

SIMULATIONS = 250

def check_positive(input_array):
    if 1 in input_array:
        return True
    else:
        return False

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return m, m - h, m + h

#########################################################
################### WEBSITE DESIGN ######################
#########################################################


################## TITLE ##################

col1, col2 = st.columns((1, 2))

with col1:
    new_title = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30; font-size:3rem;">POOL-SIZE IMPACT ON <p style="font-family:sans-serif; font-weight: bold; color:Red; font-size:3rem;">qPCR </p> <p style="font-family:sans-serif; font-weight: bold; color:#050a30; font-size:3rem;"> WORKFLOW</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    #st.title("Pool-Size impact on qPCR Workflow")

with col2:
    col2_text = '<p style="font-family:sans-serif; font-weight: bold; text-align: right; vertical-align: text-bottom; color:Blue; font-size:1rem;"> <a href="https://github.com/CFVALLS">Author: Cristian Valls </a></p>'
    st.markdown(col2_text, unsafe_allow_html=True)
    #st.title("Pool-Size impact on qPCR Workflow")

################## DESCRIPTION ##################

# with st.container():
#    st.write("This is inside the container")

col1, col2 = st.columns((1, 1))

with col1:
    text1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:2rem; margin-top: 2rem; "> Rationale</p>'
    st.markdown(text1, unsafe_allow_html=True)
    text1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem;margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">RT-PCR is the gold-standard laboratory technique for identifying SARS-CoV-2 in a clinical setting. However, the high demand for this technique produced a deficit in the supply chain of different reactive required to perform qPCR. One method to maximize the reagents for qPCR is by ‘Pooling samples’. This has been used in other screening protocols and has also been proposed for the detection of SARS-CoV-2. </p>'
    st.markdown(text1, unsafe_allow_html=True)
    text2 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;"> Sample pooling is the method by which multiple specimens are extracted using one RNA isolation kit and then processed as a single PCR test without significant loss of sensitivity.</p>'
    st.markdown(text2, unsafe_allow_html=True)
    text3 = '<p style="font-family:sans-serif; font-weight: bold; color:Red ;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">  This Streamlit App shows how many pools per sample are ideal to maximize reagents in a one-stage pool strategies (i.e., pool samples, if positive, run samples individually) </p>'
    st.markdown(text3, unsafe_allow_html=True)
    text4 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30;font-size:2rem; margin-top: 1rem; "> References</p>'
    st.markdown(text4, unsafe_allow_html=True)

    reference_1 = '<p style="font-family:sans-serif; font-weight: bold; color:#050a30; ;font-size:1rem; margin-left: 0.5rem;margin-right: 0.5rem;text-align: justify;">  2021 Apr 17;21(1):360. doi: 10.1186/s12879-021-06061-3.</p>'
    st.markdown(reference_1, unsafe_allow_html=True)


with col2:
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

#############################################################################

label = "Samples per Pool"
POOL_SIZE = st.slider(label, min_value=2, max_value=10, value=5, step=1)

label_2 = "Population Size (Total number of samples to process) "
SAMPLE_SIZE = st.slider(label_2, min_value=100,
                        max_value=100000, value=5000, step=100)

label_3 = "Positivity Rate"
POSITIVITY = st.slider(label_3, min_value=1.0,
                       max_value=25.0, value=5.0, step=0.1)

POSITIVITY = POSITIVITY / 100

# Execute Button
button = st.button('Register')

# Create populations

sample_distribution = np.random.binomial(SAMPLE_SIZE, POSITIVITY, SIMULATIONS)


#########################################################
################### Stat Analysis #######################
#########################################################

trial = 0
total_extractions = []
while trial < len(sample_distribution):
    positive_proportion = (sample_distribution[trial])
    negative_proportion = (SAMPLE_SIZE - sample_distribution[trial])
    trial = trial + 1
    # print(trial)

    # Create Array of positive & negatie Samples
    arr = np.array([0] * negative_proportion + [1] * (positive_proportion))
    random.shuffle(arr)
    # print(arr)

    # Divide Array subarrays from size POOL_SIZE
    splitted_arr = np.array_split(arr, (SAMPLE_SIZE / POOL_SIZE))
    num_pools = len(splitted_arr)
    # print(splitted_arr)

    # check positives in pool
    positive_pool = 0

    for i in splitted_arr:
        if check_positive(i):
            positive_pool = 1 + positive_pool

    # print(positive_pool)
    # print(num_pools)

    extractions = num_pools + (positive_pool * POOL_SIZE)
    total_extractions.append(extractions)

    #print("number of extractions: {ext} in a total of {smp} samples , pooling with {pool} samples per pool".format(ext = extractions , smp = SAMPLE_SIZE, pool= POOL_SIZE ))

#print("mean extractions in {SIMULATIONS} simulations: {count}".format(SIMULATIONS = SIMULATIONS, count = sum(total_extractions)/SIMULATIONS))

mean_extractions = round(sum(total_extractions) / SIMULATIONS, 0)
mean, h_lower, h_high = mean_confidence_interval(total_extractions)
print(h_lower, h_high)

# Plot Construction
#figure = plt.hist(total_extractions, density=False,color ='green',alpha = 0.7)
#plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)

header2 = "Plot interpretation: X-axis corresponds to number of RNA extractions, y-axis corresponds to number of simulations. Hence, distribution of extractions in the populations simulated "
st.header(header2)


col3, col4 = st.columns((1, 1))

with col3:
    fig, ax = plt.subplots()
    ax.hist(total_extractions, density=False, color='red', alpha=0.5)
    plt.xlabel("Num of Extraccion")
    plt.ylabel("Num of Populations")
    plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)

    st.pyplot(fig)

    # Create an empty dataframe
    data = pd.DataFrame(columns=["Pool Size", "SAMPLE_SIZE",
                                 "POSITIVITY", "Number Of Extractions", "simulation's std"])

    # with every interaction, the script runs from top to bottom
    # resulting in the empty dataframe
    # st.dataframe(data)

    # persist state of dataframe
    session_state = SessionState.get(df=data)

with col4:

    if button:
        # update dataframe state
        session_state.df = session_state.df.append({"Pool Size": round(int(POOL_SIZE), 0), "SAMPLE_SIZE": round(int(
            SAMPLE_SIZE), 0), "POSITIVITY": POSITIVITY, "Number Of Extractions": round(mean_extractions, 0), "simulation's std": np.std(total_extractions)}, ignore_index=True)
        st.dataframe(session_state.df)


# st.table(df)
