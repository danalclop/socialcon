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
data_path = project_path + 'Scatterplot/Processing-and-Analysis/Importable-Data/'
des_path = project_path + 'Scatterplot/Processing-and-Analysis/Analysis-Data/'

# Read the data
df = pd.read_csv(os.path.join(data_path + 'subjective-ratings-affect-likableness-ord.csv'), sep=';')
x = df["affect"]
y = df["likableness"]

# ============================================================================
# PLOT
# ============================================================================

# Set up styling presets
sns.set(style="white", color_codes=True)

# Create and save the figure
g = sns.jointplot(x="affect", y="likableness", hue="category", data=df, height=10, ratio=3,
                  marginal_kws=dict(bins=15),
                  annot_kws=dict(stat="r"), alpha=0.4,
                  linewidth=1)  # s=40, edgecolor="w",
plt.savefig(os.path.join(des_path + '19-05-26-results-affect_likableness-scatterplot02.png'), dpi=150)




# ============================================================================

# Set up styling presets
sns.set(style="white", color_codes=True)
flatui = ["#8f517d", "#dca8ab", "#407f76", "#d0e2c9"]
cmap = sns.color_palette(flatui)
# cmap = sns.color_palette("Paired", 4)
# Create and save the figure
g = sns.lmplot(x="affect", y="likableness", hue="category", data=df,
                    fit_reg=False, height=10, palette=cmap)
plt.savefig(os.path.join(des_path + '19-05-26-results-affect_likableness-scatterplot02.png'), dpi=150)
