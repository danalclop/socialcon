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

project_path = '/Users/danalclop/Google Drive/1905-SOCIALCON/Figures/05Representational-Similarity/'
data_path = project_path + '4CLASSES/Boxplot/Processing-and-Analysis/Importable-Data/'
des_path = project_path + '4CLASSES/Boxplot/Processing-and-Analysis/Analysis-Data/'
roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1']

# ============================================================================
# READ THE DATA
# ============================================================================
df = pd.read_csv(os.path.join(data_path + 'RSAindivRatingsindivBOLD.csv'), sep=';')  # , index_col=0
df = df.sort_values("roi")

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set_style("white")  # , {"axes.facecolor": ".9"}
sns.despine()
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
fig, ax = plt.subplots(figsize=(15, 15))
ax = sns.boxplot(x='roi', y='rsa', hue='category', data=df, palette=palette1)  # inner=None, color='.8'
ax = sns.stripplot(x='roi', y='rsa', hue='category', data=df, palette=palette2,
                   jitter=True, linewidth=1, dodge=True, alpha=.65)
ax.set(ylim=(-0.10, 0.30))
ax.set_xticklabels(roi_order, rotation='45')
plt.savefig(os.path.join(des_path + '4classes-decoding-boxplot-control.png'), dpi=300)
