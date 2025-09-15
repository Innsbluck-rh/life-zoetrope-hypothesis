# examples/02_coincident_frames.py
import numpy as np
from model.sampling import dirac_comb_times, coincedent_frames_times
from viz.figures import fig_coincident_timeline

TL, TD = 1.0, 1.5   # 例: 2:3 で周期的に重なる
t_end = 12.0
tL = dirac_comb_times(TL, 0, t_end)
tD = dirac_comb_times(TD, 0, t_end)
hits = coincedent_frames_times(TL, TD, t_end)
fig_coincident_timeline(tL, tD, hits, "fig_coincident.svg")
