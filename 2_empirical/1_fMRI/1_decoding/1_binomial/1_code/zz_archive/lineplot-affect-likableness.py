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

project_path = '/Users/danalclop/Desktop/1905-SOCIALCON/Figures/Decoding-Accuracy/'
data_path = project_path + 'AFFECT-LIKABLENESS/Processing-and-Analysis/Importable-Data/'
des_path = project_path + 'AFFECT-LIKABLENESS/Processing-and-Analysis/Analysis-Data/'
roi_order = ['LITG', 'IFG', 'PREC', 'ATL', 'APFC', 'AI', 'ACC', 'PCC', 'V1']

# Read the data
df = pd.read_csv(os.path.join(data_path + 'affect_likableness.csv'), sep=';')

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
palette = sns.color_palette("mako_r", 2)
sns.set_style("darkgrid", {"axes.facecolor": ".9"})

# Create and save the figure
ax = sns.lineplot(x='roi', y='accuracy', hue='class', data=df, palette=palette)
ax.set(ylim=(0.45, 0.75))
ax.set_xticklabels(roi_order, rotation='45')
plt.savefig(os.path.join(des_path + '19-05-25-results-affect_likableness.png'), dpi=150)
