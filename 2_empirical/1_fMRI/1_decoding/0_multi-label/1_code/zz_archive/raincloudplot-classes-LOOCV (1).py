
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import ptitprince as pt

#sns.set(style="darkgrid")
#sns.set(style="whitegrid")
sns.set_style("white")
#sns.set(style="whitegrid",font_scale=2)
import matplotlib.collections as clt

df = pd.read_csv(os.path.join('Downloads/', 'resultsLOOCVlikableness20_labelled.csv'), index_col=0)

"""
roi_order = ['LTL', 'IFG', 'Prec', 'ATL', 'aPFC', 'Ins', 'ACC', 'PCC', 'V1', 'PM']
cols = roi_order
df = df[cols]
"""

clean_df = pd.melt(df, var_name='ROI', value_name='Classification accuracy')

classes_palette = ['#62BFCD', '#62BFCD', '#62BFCD', '#5B839C', '#5B839C', '#8595C4', '#8595C4', '#8595C4', '#D5DCE2', '#D5DCE2']
affect_palette = ['#FF9300', '#FF9300', '#FF9300', '#FF9C54', '#FF9C54', '#FFAA8A', '#FFAA8A', '#FFAA8A', '#FFBFBB', '#FFBFBB']
likableness_palette = ['#009FDA', '#009FDA', '#009FDA', '#418DD7', '#418DD7', '#6979CC', '#6979CC', '#6979CC', '#8862B6', '#8862B6']

bimodal_palette = ['#FF9300', '#009FDA']

dx = 'ROI'; dy = 'Classification accuracy'; dhue = 'Class'; ort = 'h'; pal = bimodal_palette; sigma = .2

dx="group"; dy="score"; dhue = "gr2"; ort="h"; pal = "Set2"; sigma = .2

#f, ax = plt.subplots(figsize=(5, 10))

ax = pt.RainCloud(x = dx, y = dy, hue = dhue, data = df, palette = pal, bw = sigma, width_viol = 0.9, figsize = (40,10), orient = ort, alpha=.65)  # pointplot = True  # , move = .3

  # orient = ort)

ax.set(xlim=(0.3, 0.9))
# ax.set(ylim=(0.2, 0.6))
sns.despine()
plt.show()

plt.tight_layout()
