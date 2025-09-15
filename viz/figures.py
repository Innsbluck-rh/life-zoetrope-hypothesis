# viz/figures.py
import numpy as np
import matplotlib.pyplot as plt
from .styles import minimalist, save_svg

def fig_zoetrope_cross_section(life_slits: int, death_slits: int, path: str):
    fig, ax = plt.subplots(figsize=(5,5))
    minimalist(ax)
    r1_in, r1_out = 0.9, 1.2
    r2_in, r2_out = 1.35, 1.65
    th = np.linspace(0, 2*np.pi, 300)
    ax.plot(r1_in*np.cos(th), r1_in*np.sin(th))
    ax.plot(r1_out*np.cos(th), r1_out*np.sin(th))
    ax.plot(r2_in*np.cos(th), r2_in*np.sin(th))
    ax.plot(r2_out*np.cos(th), r2_out*np.sin(th))
    # slits
    for k in range(life_slits):
        ang = 2*np.pi*k/life_slits
        ax.plot([r1_in*np.cos(ang), r1_out*np.cos(ang)],
                [r1_in*np.sin(ang), r1_out*np.sin(ang)], linewidth=1.2)
    for k in range(death_slits):
        ang = 2*np.pi*k/death_slits
        ax.plot([r2_in*np.cos(ang), r2_out*np.cos(ang)],
                [r2_in*np.sin(ang), r2_out*np.sin(ang)], linewidth=1.2)
    ax.set_aspect("equal"); ax.set_xlim(-2,2); ax.set_ylim(-2,2)
    save_svg(fig, path)

def fig_strobo_phase(angles: np.ndarray, title: str, path: str):
    """angles: 連続フレームの“見かけ角”列（モデルで作る）"""
    fig, ax = plt.subplots(figsize=(5,5))
    minimalist(ax)
    R = 1.0
    th = np.linspace(0, 2*np.pi, 360)
    ax.plot(R*np.cos(th), R*np.sin(th))
    # フレームを線で
    for a in angles:
        ax.plot([0, R*np.cos(a)], [0, R*np.sin(a)], linewidth=1.4)
    ax.text(0, R+0.2, title, ha="center", va="bottom")
    ax.set_aspect("equal"); ax.set_xlim(-1.3,1.3); ax.set_ylim(-1.3,1.3)
    save_svg(fig, path)

def fig_coincident_timeline(tL: np.ndarray, tD: np.ndarray, coinc: np.ndarray, path: str):
    fig, ax = plt.subplots(figsize=(7,2.2))
    ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.hlines(0.7, 0, max(tL.max(), tD.max()) if len(tD)>0 else tL.max())
    ax.hlines(0.3, 0, max(tL.max(), tD.max()) if len(tD)>0 else tL.max())
    for t in tL: ax.vlines(t, 0.7, 0.85, linewidth=1.2)
    for t in tD: ax.vlines(t, 0.3, 0.45, linewidth=1.2)
    for t in coinc: ax.plot([t],[0.5], marker='o')
    ax.text(-0.1, 0.85, "life", ha="right", va="bottom")
    ax.text(-0.1, 0.45, "death", ha="right", va="bottom")
    save_svg(fig, path)
