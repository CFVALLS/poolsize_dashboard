import streamlit as st
import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import SessionState

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

header = "Esta webApp simula la cantidad de extracciones que se realizaran considerando una determinada cantidad de muestras por pool y una determinada positividad"
st.header(header)

label = "Escoger muestras por Pool"
POOL_SIZE = st.slider(label, min_value=2, max_value=10,value=5, step=1)

label_2 = "Escoger Numero de muestras por simulacion"
SAMPLE_SIZE = st.slider(label_2, min_value=100, max_value=100000,value=5000, step=100)

label_3 = "Seleccionar Positividad"
POSITIVITY = st.slider(label_3, min_value=1.0, max_value=25.0, value=5.0,step=0.1)
POSITIVITY = POSITIVITY/100

# Execute Button
button = st.button('Registrar')

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

mean_extractions = round(sum(total_extractions)/SIMULATIONS,0)

#Plot Construction
#figure = plt.hist(total_extractions, density=False,color ='green',alpha = 0.7)
#plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)

header2 = "El grafico inferior muestra la cantidad de extracciones obtenidas en 250 simulaciones. Eje X corresponde a la cantidad de extracciones que se hicieron en cada Trial. Eje Y corresponde a la frecuencia correspondiente"
st.header(header2)

fig, ax = plt.subplots()
ax.hist(total_extractions, density=False,color ='red',alpha = 0.5)
plt.xlabel("Numero de extracciones por simulacion")
plt.ylabel("Frequencia")
plt.axvline(mean_extractions, color='k', linestyle='dashed', linewidth=1)

st.pyplot(fig)

# data = {'Pool Size':[POOL_SIZE],'Sample Size':[SAMPLE_SIZE],'Positivity':[POSITIVITY],"average extractions":[mean_extractions]}
#
# df = pd.DataFrame(data)
#
# # persist state of dataframe
# session_state = SessionState.get(df=data)
#
# if button:
#     # update dataframe state
#     session_state.df = session_state.df.append({'Pool Size': POOL_SIZE , 'Sample Size':SAMPLE_SIZE,'Positivity':POSITIVITY,"average extractions":mean_extractions}, ignore_index=True)
#     st.dataframe(session_state.df)

# Create an empty dataframe
data = pd.DataFrame(columns=["Pool Size" , "SAMPLE_SIZE" , "POSITIVITY", "Number Of Extractions"])

# with every interaction, the script runs from top to bottom
# resulting in the empty dataframe
# st.dataframe(data)

# persist state of dataframe
session_state = SessionState.get(df=data)

if button:
    # update dataframe state
    session_state.df = session_state.df.append({"Pool Size": POOL_SIZE , "SAMPLE_SIZE" : SAMPLE_SIZE,"POSITIVITY" : POSITIVITY , "Number Of Extractions" : mean_extractions}, ignore_index=True)
    st.dataframe(session_state.df)


#st.table(df)

author = "Author: Cristian Valls"
st.header(author)
