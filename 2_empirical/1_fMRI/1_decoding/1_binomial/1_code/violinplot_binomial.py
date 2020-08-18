# ============================================================================
# IMPORTS
# ============================================================================

import os
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import patches
import seaborn as sns

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

project_path = '/Users/danalclop/Google Drive/Research/BCBL/SOCIALCON /'
data_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial/0_data/'
des_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial//3_output/figures/'
roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1']

# Read the data
df_item = pd.read_csv(os.path.join(data_path + '2_tidy_labelled_binomial_chunkCV.csv'), sep=';').sort_values(by=['roi', 'class'])

df_item["accuracy"] = df_item["accuracy"].str.replace(",",".").astype(float)

# ========================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_context("poster", font_scale=1, rc={"lines.linewidth": 3})
sns.set_style('white')

# pal = ["#E5323B", "#2E4052"]
pal = ["#D5727A", "#666F79"]

# Create the figure
fig, ax = plt.subplots(figsize=(15, 8))
#ax.set_title('')

ax = sns.violinplot(x='roi', y='accuracy', hue='class', data=df_item, inner='quartile', cut=0, split=True, palette=pal, color='b', saturation=5)

rect = patches.Rectangle(
    xy=(ax.get_xlim()[0], 0.0),  # lower left corner of box: beginning of x-axis range & y coord)
    width=ax.get_xlim()[1]-ax.get_xlim()[0],  # width from x-axis range
    height=0.5357,
    color='gray', alpha=0.1, ec='black'
)
ax.add_patch(rect)

ax.set(ylim=(0.45, 0.85))
ax.set_xticklabels(roi_order, rotation='0')
ax.set(xlabel="")
ax.set(ylabel="Correct classification rate\n")
sns.despine()
ax.legend().set_visible(False)
ax.locator_params(nbins=6, axis='y')

plt.savefig(os.path.join(des_path + 'affecet-likableness-decoding-boxplot.png'), dpi=300)
