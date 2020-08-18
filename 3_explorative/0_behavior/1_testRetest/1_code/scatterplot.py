"""This script calculates the Pearson correlation coefficient of the pre-
and post-scanning behavioral ratings of the stimuli used in SOCIALCON
"""

import os

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('/bcbl/home/public/Consciousness/socialcon/figures/scatterplots/likableness/')

behav_data = pd.read_csv('data/pre_post_LIKABLENESS_data.csv', index_col=0)

# Before computing the Pearson correlation coefficient, let's first get the
# a list with the labels of the concepts

concept_labels = []
for c in behav_data.columns[0:36]:
    concept_labels.append(c)


# Now loop through the pre- and post-scanning rating of each stimuli and
# calculate the Pearson correlation coefficient

pre_post_LIKABLENESS_corcoef = []
for i in range(0, 36):
    print(" ")
    print("Calculating the Pearson correlation coefficient of the ratings of " + str(concept_labels[i-1]))
    corcoef = behav_data.iloc[:, i].corr(behav_data.iloc[:, i+36])
    pre_post_LIKABLENESS_corcoef.append(corcoef)
    print("...")
    print("Done! The Pearson correlation coefficient for " + str(concept_labels[i-1]) + " is " + str(corcoef))

pre_post_LIKABLENESS_mean_corcoef = np.mean(pre_post_LIKABLENESS_corcoef)
print(" ")
print("### ### ### ### ### ### ###")
print(" ")
print("The mean Pearson correlation coeficient of all ratings is " + str(pre_post_LIKABLENESS_mean_corcoef))


# Let's create a DataFrame to store these results

Pearson_corcoef = pd.DataFrame(
    {'Concept': concept_labels,
     'Pearson_corcoef': pre_post_LIKABLENESS_corcoef
    })

Pearson_corcoef.to_csv('pre_post_LIKABLENESS_results.csv', header=True)

# Finally, let's make some plots to visually inspect the reliability of
# the behavioral ratings of our concepts

g = sns.jointplot("Resentido/a", "2Resentido/a", data=behav_data, kind="reg",
                  xlim=(-10, 110), ylim=(-10, 110), color="#1d2137", size=7,
                  marginal_kws=dict(bins=10, rug=True))
