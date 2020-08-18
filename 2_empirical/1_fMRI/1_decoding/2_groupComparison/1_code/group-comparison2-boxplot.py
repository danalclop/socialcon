# ============================================================================
# IMPORTS
# ============================================================================

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================================
# READ THE DATA
# ============================================================================

df = pd.read_csv('affect-likableness.csv', sep=";")

# ============================================================================
# PLOT
# ============================================================================
sns.set_context("notebook", font_scale=2.5)
sns.set_style('white')
palette1 = ["#62BFCD", "#8595C4"]

fig, ax = plt.subplots(figsize=(4, 15))
ax = sns.boxplot(x='category', y='accuracy', data=df_affect, palette=palette1, linewidth=3.0)

ax.set(ylim=(0.4, 0.85))
# ax.legend_.remove()
ax.set(xlabel="")
ax.set(ylabel="Decoding accuracy\n")
sns.despine()
labels = ['SEM', 'SOC']
ax.set_xticklabels(labels, rotation='45')
ax.set_title('Affect\n')
ax.locator_params(nbins=5, axis='y')

plt.savefig('group-comparinson-boxplot2.png', dpi=300)
