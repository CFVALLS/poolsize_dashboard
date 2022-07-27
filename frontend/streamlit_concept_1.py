import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import SessionState
import scipy.stats


################################################################
################### FUNCTIONS AND CONSTANTS ####################
#################################################################

POSITIVITY = 0.05
SIMULATIONS = 1000

def simulate_population(pool_size,positivity,samples):
    """
        input n: pool size
              p: positivity
           sims: number of samples
        returns: population    """
    population = np.random.binomial(pool_size, positivity, samples)
    return population


#################################################################
###################         SCRIPT           ####################
#################################################################

x = simulate_population(pool_size = 5, positivity = POSITIVITY,samples = 1000)
print(x)
plt.hist(x)
plt.show()
