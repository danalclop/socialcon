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

project_path = '/Users/danalclop/Desktop/1905-SOCIALCON/Figures/Subjective-Ratings/'
data_path = project_path + 'Hexbin/Processing-and-Analysis/Importable-Data/'
des_path = project_path + 'Hexbin/Processing-and-Analysis/Analysis-Data/'

# Read the data
df = pd.read_csv(os.path.join(data_path + 'melt-sorted-subjective-ratings.csv'), sep=';')
x = df["affect"]
y = df["likableness"]

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set(style="white", color_codes=True)

# Create and save the figure
joint_kws=dict(gridsize=15)
g = sns.jointplot("affect", "likableness", data=df, kind="hex", joint_kws= joint_kws,
                  height=10, ratio=3, marginal_kws=dict(bins=25),
                  annot_kws=dict(stat="r"), linewidth=1)
plt.savefig(os.path.join(des_path + '19-05-26-results-affect_likableness-hexbin.png'), dpi=150)
