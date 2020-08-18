# ============================================================================
# IMPORTS
# ============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# READ THE DATA
# ============================================================================

df = pd.read_csv('19-05-30-group-comparison.csv', index_col=0)

# ============================================================================
# PLOT
# ============================================================================

sns.set_style("white")  # , {"axes.facecolor": ".9"}
sns.despine()
palette1 = ["#62BFCD", "#8595C4"]
palette2 = ["#53E2D9", "#AC83C5"]

fig, ax = plt.subplots(figsize=(2, 15))
ax = sns.boxplot(x='category', y='accuracy', hue='category', data=df,
                    palette=palette1)
ax = sns.stripplot(x='category', y='accuracy', hue='category', data=df,
                   jitter=True, linewidth=1, dodge=True, alpha=.65,
                   palette=palette2)
ax.set(ylim=(0.2, 0.6))
# ax.set_xticklabels(roi_order, rotation='45')
plt.savefig('group-comparinson-boxplot2.png', dpi=300)
