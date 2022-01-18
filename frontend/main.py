import streamlit as st
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

###### CONSTANTS#####

SIMULATIONS = 250

###### FUNCTIONS #####

def check_positive(input_array):
    if 1 in input_array:
        return True
    else:
        return False

#############################################################################
st.title('Distribucion de extracciones segun numero de muestras por Pool')

header = "Calculo de Extracciones segun muestras por pool"
st.header(header)


label = "Escoger muestras por Pool"
POOL_SIZE = st.slider(label, min_value=2, max_value=10,value=5, step=1)

label_2 = "Escoger Numero de muestras por simulacion"
SAMPLE_SIZE = st.slider(label_2, min_value=100, max_value=100000,value=5000, step=100)

label_3 = "Seleccionar Positividad"
POSITIVITY = st.slider(label_3, min_value=1.0, max_value=25.0, value=5.0,step=0.1)
POSITIVITY = POSITIVITY/100

# Create populations

sample_distribution = np.random.binomial(SAMPLE_SIZE , POSITIVITY , SIMULATIONS)


############### Population analysis ####################
trial = 0
total_extractions = []
while trial < len(sample_distribution):
    positive_proportion = (sample_distribution[trial])
    negative_proportion = (SAMPLE_SIZE - sample_distribution[trial])
    trial = trial + 1
    #print(trial)

    #Create Array of positive & negatie Samples
    arr = np.array([0] * negative_proportion + [1] * (positive_proportion))
    random.shuffle(arr)
    #print(arr)

    #Divide Array subarrays from size POOL_SIZE
    splitted_arr = np.array_split(arr, (SAMPLE_SIZE/POOL_SIZE))
    num_pools = len(splitted_arr)
    #print(splitted_arr)

    #check positives in pool
    positive_pool = 0

    for i in splitted_arr:
        if check_positive(i):
            positive_pool = 1 + positive_pool

    #print(positive_pool)
    #print(num_pools)

    extractions = num_pools + (positive_pool * POOL_SIZE)
    total_extractions.append(extractions)

    #print("number of extractions: {ext} in a total of {smp} samples , pooling with {pool} samples per pool".format(ext = extractions , smp = SAMPLE_SIZE, pool= POOL_SIZE ))

print("mean extractions in {SIMULATIONS} simulations: {count}".format(SIMULATIONS = SIMULATIONS, count = sum(total_extractions)/SIMULATIONS))

mean_extractions = sum(total_extractions)/SIMULATIONS

#Plot Construction
#figure = plt.hist(total_extractions, density=False,color ='green',alpha = 0.7)
#plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)


fig, ax = plt.subplots()
ax.hist(total_extractions, density=False,color ='red',alpha = 0.5)
plt.xlabel("Numero de extracciones por simulacion")
plt.ylabel("Frequencia")
plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)

st.pyplot(fig)


author = "Author: Cristian Valls"
st.header(author)
