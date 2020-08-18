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

project_path = '/Users/danalclop/Google Drive/1905-SOCIALCON/Figures/01Subjective-Ratings/'
data_path = project_path + 'Stripplot/Processing-and-Analysis/Importable-Data/'
des_path = project_path + 'Stripplot/Processing-and-Analysis/Analysis-Data/'

# ============================================================================
# Read the data
soc_behav = pd.read_csv(os.path.join(data_path + 'subjective-ratings-affect-likableness-ord.csv'), sep=';')
df = pd.melt(soc_behav, "class", var_name="rating")

# ============================================================================
# PLOT
# ============================================================================

# Set up the styling
# palette = ["#001B74", "#A8382E"]

# palette = sns.color_palette("mako_r", 2)

# Initialize the figure
f, ax = plt.subplots(figsize=(20,15))
sns.despine(bottom=True, left=True)

# Show each observation with a scatterplot
sns.stripplot(x="value", y="rating", hue="class",
              data=df, dodge=True, jitter=True,
              alpha=.25, zorder=1)  # , palette=palette

# Show the conditional means
sns.pointplot(x="value", y="rating", hue="class",
              data=df, dodge=.532, join=False,  # palette=palette,
              markers="d", scale=.75, ci=None)

# Improve the legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[2:], labels[2:], title="Class",
          handletextpad=0, columnspacing=1,
          loc="upper left", ncol=3, frameon=True)
plt.savefig(os.path.join(des_path + '19-05-26-results-affect_likableness02.png'), dpi=300)
