# examples/03_jitter_flip.py
import numpy as np
from model.world import World
from model.sampling import View, nearest_branch_ratio
import matplotlib.pyplot as plt

w = World(omega0=10.0)
T0 = 2*np.pi / 10.0     # ほぼ同調
etas = np.linspace(-0.05, 0.05, 300)

wapps = []
for e in etas:
    T = T0*(1+e)
    view = View(T=T)
    k = nearest_branch_ratio(w.omega0, view.Omega)
    wapps.append(w.omega0 - k*view.Omega)

plt.figure(figsize=(6,3))
plt.plot(etas, wapps)
plt.axhline(0, linestyle='--')
plt.xlabel("jitter η"); plt.ylabel("apparent ω")
plt.title("Zero crossing near synchrony")
plt.savefig("fig_jitter.svg", bbox_inches="tight")

plt.show()