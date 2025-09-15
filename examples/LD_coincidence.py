# examples/02_coincident_frames.py
from matplotlib import pyplot as plt
import numpy as np
from scipy.fft import fft
from viz.styles import default_style, save_svg

default_style()

N = 20

T_L = 2
T_D = 3

DiracComb_L = np.zeros(N)
DiracComb_L[:] = np.nan
DiracComb_L[::T_L] = 1

DiracComb_D = np.zeros(N)
DiracComb_D[:] = np.nan
DiracComb_D[::T_D] = 1

T_LD = T_L * T_D
DiracComb_LD = np.zeros(N)
DiracComb_LD[:] = np.nan
DiracComb_LD[::T_LD] = 1

fig = plt.figure(figsize=(4, 2))

plt.stem(DiracComb_L,
         label="Life",
         linefmt='m:',
         markerfmt='^',
         basefmt="gray")
plt.stem(DiracComb_D,
         label="Death",
         linefmt='b:',
         markerfmt='^',
         basefmt="gray")
plt.stem(DiracComb_LD,
         label="Coincident",
         linefmt='r',
         markerfmt='^',
         basefmt="gray")

plt.legend(loc='upper center',
           bbox_to_anchor=(0.5, -0.3),
           ncol=3,
           markerscale=4)
plt.ylim([0, 1.1])
plt.yticks([0, 1.0])
plt.ylabel("Shuttering [a.u.]")
plt.xlabel("Time [a.u.]")

plt.title("L/D Coincidence by common multiples")
plt.savefig("fig_LD_coincidence.svg", bbox_inches="tight")
plt.savefig("fig_LD_coincidence.png", bbox_inches="tight")
plt.show()

# plt.figure()
# f = np.linspace(0, 1, N)
# plt.stem(f, 1 / N *
#          abs(DiracComb_f))  # Actually there is a factor N in the fft
# _ = plt.ylim([0, 1.1 * 1 / L0])
# plt.xlabel("Frequency")
