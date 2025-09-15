# viz/styles.py
import matplotlib.pyplot as plt

custom_style = {
    'figure.facecolor': '#0A0A0A',
    'axes.facecolor': '#0A0A0A',
    'axes.edgecolor': '#ffffff',
    'axes.labelcolor': '#ffffff',
    'text.color': 'white',
    'xtick.color': '#ffffff',
    'ytick.color': '#ffffff',
    'lines.color': '#ffffff',
    'patch.edgecolor': '#0A0A0A',
    'grid.color': '#0A0A0A',
    'grid.linestyle': '--',
    'grid.alpha': 0.4,
    'legend.edgecolor': '#ffffff',
    'legend.facecolor': '#202020',
    'legend.framealpha': 0  ,
    'lines.linewidth': 1.5,
    'lines.markersize': 5,
}


def default_style():
    plt.rcParams["font.family"] = "04b03"
    plt.rcParams["font.size"] = 8
    plt.style.use(custom_style)


def minimalist(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_visible(False)


def save_svg(fig, path):
    fig.savefig(path, bbox_inches="tight")
