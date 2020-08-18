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
data_path = project_path + '4CLASSES/Processing-and-Analysis/Importable-Data/'
des_path = project_path + '4CLASSES/Processing-and-Analysis/Analysis-Data/'
roi_order = ['LITG', 'IFG', 'PREC', 'ATL', 'APFC', 'AI', 'ACC', 'PCC', 'V1']

# Read the data
df = pd.read_csv(os.path.join(data_path + '4classes.csv'), sep=';')

# ============================================================================
# PLOT
# ============================================================================

sns.set()
# Set up styling presets
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.despine()

# Create and save the figure
ax = sns.lineplot(x='roi', y='accuracy', data=df)
ax.set(ylim=(0.2, 0.6))
ax.set_xticklabels(roi_order, rotation='45')
plt.savefig(des_path + '19-05-25-results-4classes.png', dpi=150)
