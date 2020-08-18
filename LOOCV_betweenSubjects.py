#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:41:53 2019

@author: dalcala

To be executed from the following path:
    '~/public/Consciousness/socialcon/code/MVPAscripts'

This script reads out the output from the leave-one-out classification at
subject level, fetches the classification accuracies and computes a
between-subjects accuracy for each ROI.
"""

import os
from glob import glob
import pickle

from scipy.stats import ttest_1samp
from statsmodels.sandbox.stats.multicomp import fdrcorrection0
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# Set up plotting style
# ============================================================================

sns.set(style='ticks')

# ============================================================================
# Declare a helper function to load and preprocess the input data
# ============================================================================

def format_results(res_path):

    # ========================================================================
    # Fetch results from the classification problem and do some data cleaning
    # ========================================================================

    results = np.zeros((30,10))
    s_count = 0
    for subj in glob(os.path.join(res_path, '*')):
        print(subj)
        subj_dat = np.load(os.path.join( subj, 'final_results.npy'))

        index = 0
        subj_acc_dat = np.zeros((10,))
        for column in subj_dat:
            roi_acc = np.mean(column)
            subj_acc_dat[index] = roi_acc
            index += 1
        print("Mean classification accuracies for each ROI in {} are: ".format(subj).format)
        print(subj_acc_dat)

        results[s_count,:] = subj_acc_dat
        s_count += 1

    return results

def main():
    res_path = os.path.join('..', '..', 'data', 'LOOCV_AFFECT/')
    formatted = format_results(res_path)

    cur_columns = ['ACC', 'LTL', 'ATL', 'IFG', 'Ins', 'PCC', 'aPFC', 'Prec', 'V1', 'PM']
    roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1', 'PM']
    df = df[roi_order] 

if __name__ == '__main__':
    main()