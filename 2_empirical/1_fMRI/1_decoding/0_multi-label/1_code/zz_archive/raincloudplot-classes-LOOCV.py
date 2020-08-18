
import matplotlib.collections as clt
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import ptitprince as pt

sns.set_style("white")
# sns.set(style="whitegrid",font_scale=2)

df = pd.read_csv(os.path.join('Downloads/', 'resultsLOOCVaffect_labelled.csv'),
                 index_col=0)

clean_df = pd.melt(df, var_name='ROI', value_name='Classification accuracy')

classes_palette = ['#62BFCD', '#62BFCD', '#62BFCD', '#5B839C',
                   '#5B839C', '#8595C4', '#8595C4', '#8595C4',
                   '#D5DCE2', '#D5DCE2']

affect_palette = ['#FF9300', '#FF9300', '#FF9300', '#FF9C54',
                  '#FF9C54', '#FFAA8A', '#FFAA8A', '#FFAA8A',
                  '#FFBFBB', '#FFBFBB']

likableness_palette = ['#009FDA', '#009FDA', '#009FDA', '#418DD7',
                       '#418DD7', '#6979CC', '#6979CC', '#6979CC',
                       '#8862B6', '#8862B6']

dx = 'ROI'
dy = 'Classification accuracy'
ort = 'v'
pal = affect_palette
sigma = .2
#f, ax = plt.subplots(figsize=(5, 10))

ax = pt.RainCloud(x=dx, y=dy, data=clean_df, palette=pal, bw=sigma,
                  width_viol=0.7, orient=ort, move=.3, alpha=.65)

ax.set(ylim=(0.40, 0.90))
# ax.set(ylim=(0.2, 0.6))
sns.despine()
plt.show()
