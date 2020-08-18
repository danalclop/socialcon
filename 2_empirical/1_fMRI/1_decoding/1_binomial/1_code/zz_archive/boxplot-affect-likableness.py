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
data_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial/0_data/'
des_path = project_path + '2_empirical/1_fMRI/1_decoding/1_binomial//3_output/figures/'
roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1']

# Read the data
df_binomial_chunkCV = pd.read_csv(os.path.join(data_path + 'tidy_results-affect-likableness.csv'), sep=';')
df_binomial_conceptCV = pd.read_csv(os.path.join(data_path + 'tidy_LOOCV_affect20-likableness20.csv'), sep=';')
df_binomial_chunkCV = df.sort_values("roi")

# ========================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2}) 
sns.set_style('white')

palette = ["#FF913D", "#71A6CC"]

# Create the figure
fig, ax = plt.subplots(figsize=(15, 8))
ax.set_title('Binomial classification using concept-level CV\n', fontsize=30)

ax = sns.boxplot(x='ROI', y='Classification accuracy', hue='Class', data=df_binomial_concept, palette=palette, linewidth=3.5)

rect = patches.Rectangle(
    xy=(ax.get_xlim()[0], 0.0),  # lower left corner of box: beginning of x-axis range & y coord)
    width=ax.get_xlim()[1]-ax.get_xlim()[0],  # width from x-axis range
    height=0.5357,
    color='gray', alpha=0.1, ec='black'
)
ax.add_patch(rect)

ax.set(ylim=(0.45, 1.0))
ax.set_xticklabels(roi_order, rotation='45')
ax.set(xlabel="")
ax.set(ylabel="Correct classification rate\n")
sns.despine()
plt.legend(frameon=False)
ax.locator_params(nbins=6, axis='y')

plt.savefig(os.path.join(des_path + 'affecet-likableness-decoding-boxplot.png'), dpi=300)
