

# Hue Input for Subgroups
dx="Concept"; dy="Rating"; dhue = "Class"; ort="h"; pal = ; sigma = .2


sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 0.5}) 
sns.set_style('white')

palette = ['#E5323B', '#2E4052']
f, ax = plt.subplots(figsize=(12, 10))

ax=pt.RainCloud(x = 'Concept', y = 'Rating', hue = 'Class', data = df, palette = palette, bw = .2, width_viol = .9, ax = ax, orient = 'h', alpha = .65, dodge = True)

plt.title("Subjective ratings of unaffective and highly likable concepts\n")

ax.set(xlabel="")
ax.set(ylabel="")
sns.despine()


if savefigs:
    plt.savefig(os.path.join(project_path [][][][][]'../figs/tutorial_python/figureP14.png', bbox_inches='tight')