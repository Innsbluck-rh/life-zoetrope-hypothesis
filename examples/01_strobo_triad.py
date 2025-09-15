# examples/01_strobo_triad.py
import numpy as np
from model.world import World
from model.sampling import View, apparent_omega
from viz.figures import fig_strobo_phase

w = World(omega0=2.5)         # 本当の回転
life = View(T=0.9)            # 覗き穴テンポ
wapp = apparent_omega(w.omega0, life)

# 連続フレームN枚ぶんの“見かけ角”
N = 10
angles_forward = np.cumsum(np.full(N, wapp*life.T)) % (2*np.pi)
angles_pause   = np.cumsum(np.zeros(N))             % (2*np.pi)
angles_reverse = np.cumsum(np.full(N, -abs(wapp)*life.T)) % (2*np.pi)

fig_strobo_phase(angles_forward, "Stroboscopic: Forward", "fig_forward.svg")
fig_strobo_phase(angles_pause,   "Stroboscopic: Pause",   "fig_pause.svg")
fig_strobo_phase(angles_reverse, "Stroboscopic: Reverse", "fig_reverse.svg")
