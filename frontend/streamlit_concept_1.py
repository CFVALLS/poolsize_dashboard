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
SIMULATIONS = 250
NUM_SAMPLES = 10000

def simulate_population(samples,positivity,sims):
    """
        input n: sample number
              p: positivity
           sims: number of sims
        returns: population    """
    population = np.random.binomial(samples, positivity, sims)
    return population

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

#################################################################
###################         SCRIPT           ####################
#################################################################

# 1-. generate populations according with the positivity inputted
x = simulate_population(samples = NUM_SAMPLES, positivity = POSITIVITY, sims = SIMULATIONS)

# 2-. Randomly Distribute the number of positive
