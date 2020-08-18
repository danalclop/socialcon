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
df = pd.read_csv(os.path.join(data_path + 'clean_boxplot_multiLabel_conceptCV.csv'), sep=';')  # , index_col=0
df = df.sort_values("roi")

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2}) 
sns.set_style('white')

palette = ["#62BFCD", "#5B839C", "#8595C4", "#D5DCE2"]

# Create the figure
fig, ax = plt.subplots(figsize=(15, 8))
ax.set_title('Multi-label classification using concept-level CV\n', fontsize=30)

ax = sns.violinplot(x='roi', y='accuracy', hue='category', data=df, palette=palette, linewidth=1.5)  # inner=None, color='.8'

rect = patches.Rectangle(
    xy=(ax.get_xlim()[0], 0.0),  # Lower left corner of box: beginning of x-axis range & y coord)
    width=ax.get_xlim()[1]-ax.get_xlim()[0],  # width from x-axis range
    height=0.286,
    color='gray', alpha=0.1, ec='black'
)
ax.add_patch(rect)

ax.set(ylim=(0.15,  0.85))
ax.set_xticklabels(roi_order, rotation='45')
ax.set(xlabel="")
ax.set(ylabel="Correct classification rate\n")
sns.despine()
plt.legend(frameon=False)
ax.locator_params(nbins=5, axis='y')

plt.savefig(os.path.join(des_path + 'multiLabel-chunckCV-boxplot.png'), dpi=300)
