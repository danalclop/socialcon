import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import scikit_posthocs as sp

project_path = os.path.join(os.path.join('Research', 'BCBL', 'SOCIALCON '))
data_path = os.path.join(project_path, '2_empirical', '1_fMRI', '1_decoding', '1_binomial', '0_data')

df_likable_Co = pd.read_csv('postHocTests_likableness_conceptCV.csv', sep=';', header=None)
ROIs = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1']

# Set up styling presets
sns.set_context("poster", font_scale=1, rc={"lines.linewidth": 3})
sns.set_style('white')

# Create the figure
fig, ax = plt.subplots(figsize=(15, 8))
# cmap = ['1', '#FFFFFF',  '#B4171F',  '#E5323B', '#EE767C']
# cmap = ['1', '#FFFFFF',  '#C13944',  '#D5727A', '#E7ADB2']
# cmap = ['1', '#FFFFFF',  '#131A21',  '#2E4052', '#496683']
cmap = ['1', '#FFFFFF',  '#43494F',  '#666F79', '#8D959F']

heatmap_args = {'cmap': cmap, 'linewidths': 3, 'linecolor': '0.05', 'clip_on': False, 'square': True, 'cbar_ax_bbox': [0.80, 0.35, 0.04, 0.3]}

sp.sign_plot(df_likable_Co, **heatmap_args)
plt.show()