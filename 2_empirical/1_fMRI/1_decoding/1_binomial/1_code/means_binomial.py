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
data_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial/0_data/zz_arhive/'
des_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial//3_output/figures/'

os.chdir(data_path)

# Read the data

csv_file = '2_tidy_summaryV1_binomial.csv'
df = pd.read_csv(csv_file, sep=';').sort_values(by=['class', 'ID'])
df["accuracy"] = df["accuracy"].str.replace(",",".").astype(float)

x1 = df.iloc[:,-1]
y1 = df.iloc[:,-2]

# ========================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 3}) 
sns.set_style('ticks')

pal = ["#E5323B", "#D5727A", "#2E4052", "#666F79"]

ax = sns.barplot(x=x1, y=y1, palette=pal, saturation=1)
ax = sns.barplot(x=x1, y=y1, palette=pal, linewidth=5, facecolor=(1, 1, 1, 0), errcolor=".2", edgecolor=".2")

ylabels=['', '', '', '']
ax.set(xlim=(-3, 15))
ax.set_yticklabels(ylabels)
ax.set(ylabel="")
ax.set(xlabel="\nCorrect classification rate\n(% difference from chance)\n")
sns.despine(offset=10, trim=True)
# ax.legend().set_visible(False)
ax.locator_params(nbins=6, axis='x')

# plt.savefig(os.path.join(des_path + 'affecet-likableness-decoding-boxplot.png'), dpi=300)
