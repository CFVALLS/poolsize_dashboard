#################################################################
###################         Libraries        ####################
#################################################################

#import streamlit as st
import numpy as np
from numpy import random
#import matplotlib.pyplot as plt
#import SessionState
import scipy.stats

################################################################
################### FUNCTIONS AND CONSTANTS ####################
#################################################################

POSITIVITY = 0.10
SIMULATIONS = 30  # statistical power ????
NUM_SAMPLES = 10000

def simulate_population(samples, positivity, sims):
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
    """ Confidence Interval =  x̄  +/-  t*(s/√n) """
    a = 1.0 * np.array(data)
    n = len(a)
    m = np.mean(a)
    se = scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n - 1)
    return m, m - h, m + h

###########################################################################
###################         SIMULATE SAMPLES           ###################
###########################################################################
#0- Create an oyput array to append each result = [2,4500] = [pool_size,positive_pool_n, total_extractions,  percentage_ext]
output_array = []
# 1-. generate populations according with the positivity inputted
positives_by_sampling = simulate_population(
    samples=NUM_SAMPLES, positivity=POSITIVITY, sims=SIMULATIONS)

simulation = 0
while simulation < len(positives_by_sampling):
    # 2-. Create Array of positive & negatie Samples and split by pool size
    positive_proportion = positives_by_sampling[simulation]
    negative_proportion = NUM_SAMPLES - positives_by_sampling[simulation]

    randomize_samples = np.array(
        [0] * negative_proportion + [1] * (positive_proportion))
    random.shuffle(randomize_samples)

    # 3-. Split an array into multiple sub-arrays.
    pool_dict = {}
    for pool_size in range(2, 11):
        number_of_pools = NUM_SAMPLES / pool_size
        pool_dict[pool_size] = np.array_split(randomize_samples, number_of_pools)

    # 4-. Check positivity for each pool number
    # dictionary {2:[[0,0] , [0,1]] , 3: [[0,1,0] , [0,0,0]]}
    results = {}
    for pool_size_output in pool_dict:
        array_to_check = pool_dict[pool_size_output]
        positive_pool_count = 0
        for pool in array_to_check:
            if check_positive(pool):
                positive_pool_count = positive_pool_count + 1

        results[pool_size_output] = positive_pool_count

    # 5-. Calculate number of extractions
    for key in results:
        positive_pool_n = results[key]
        pool_extractions = NUM_SAMPLES / key
        individual_extractions = positive_pool_n * key
        total_extractions = pool_extractions + individual_extractions
        #compare total extractions with individual extractions
        percentage_ext = total_extractions/NUM_SAMPLES
        output_array.append([key, positive_pool_n , total_extractions,percentage_ext])
        # print('Extractions reduced by {C} , considering  {x} total number of samples, divided in pools of {y} , {z} pools where positive, total extractions {w} '.format(
        #     x=NUM_SAMPLES, y=key, z=positive_pool_n, w=total_extractions , C = percentage_ext))
    simulation = simulation + 1

array_results = np.array(output_array)

###########################################################################
######################         EXTRACT STATS         ######################
###########################################################################
# results array : [pool_size,positive_pool_n, total_extractions,  percentage_ext]

dict_streamlit_output = {}
for i in range(2,11):
    # get array of total extractions by each pool with confidence intervals.
    total_extractions = array_results[array_results[:,0] == i][:,2]
    total_extractions_m, total_extractions_l, total_extractions_h = mean_confidence_interval(total_extractions)
    # get array of total extractions by each pool with confidence intervals.
    delta_extractions = array_results[array_results[:,0] == i][:,3]
    delta_extractions_m, delta_extractions_l, delta_extractions_h = mean_confidence_interval(delta_extractions)

    dict_streamlit_output[i] = [total_extractions_m, total_extractions_l, total_extractions_h, delta_extractions_m, delta_extractions_l, delta_extractions_h]


################ Work with dict_streamlit_output ###################
