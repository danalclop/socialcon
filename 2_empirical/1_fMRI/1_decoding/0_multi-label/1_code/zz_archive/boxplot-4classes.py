# ============================================================================
# IMPORTS
# ============================================================================

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

project_path = '/Users/danalclop/Google Drive/Research/BCBL/SOCIALCON /'
data_path = project_path + '2_empirical/1_fMRI/1_decoding/0_multi-label/0_data/'
des_path = project_path + '2_empirical/1_fMRI/1_decoding/0_multi-label/2_output/figures/'
roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1']

# ============================================================================
# READ THE DATA
# ============================================================================
df = pd.read_csv(os.path.join(data_path + 'clean_boxplot_4classes.csv'), sep=';')  # , index_col=0
df = df.sort_values("roi")

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2}) 
sns.set_style('white') 

palette1 = ["#62BFCD", "#5B839C", "#8595C4", "#D5DCE2"]
palette2 = ["#53E2D9", "#68A1C1", "#AC83C5", "#FFFFFF"]
# semantic1 = ["#62BFCD"]
# semantic2 = ["#53E2D9"]
# social1 = ["#8595C4"]
# social2 = ["#AC83C5"]
# intersec1 = ["#5B839C"]
# intersec2 = ["#68A1C1"]
# control1 = ["#D5DCE2"]
# control2 = ["#FFFFFF"]

# Create and save the figure
fig, ax = plt.subplots(figsize=(15, 8))
ax = sns.boxplot(x='roi', y='accuracy', hue='category', data=df,
                 palette=palette1, linewidth=2.5)  # inner=None, color='.8'
ax = sns.stripplot(x='roi', y='accuracy', hue='category', data=df,
                   palette=palette2, jitter=True, linewidth=1, dodge=True,
                   alpha=.65)
# ax.set(ylim=(0.2, 0.6))
ax.legend_.remove()
ax.set_xticklabels(roi_order, rotation='45')
ax.set(xlabel="")
ax.set(ylabel="Decoding accuracy\n")
sns.despine()
plt.legend(frameon=False)
plt.savefig(os.path.join(des_path + 'multiLabel-chunckCV-boxplot.png'), dpi=300)
