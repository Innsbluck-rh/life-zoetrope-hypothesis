# model/sampling.py
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class View:
    T: float  # slit period (life: T_L, death: T_D)

    @property
    def Omega(self) -> float:
        return 2*np.pi / self.T

def dirac_comb_times(T: float, t_start: float, t_end: float) -> np.ndarray:
    """覗き穴の時刻列（整数列）だけ返す。"""
    n0 = int(np.ceil(t_start / T))
    n1 = int(np.floor(t_end / T))
    return np.arange(n0, n1+1) * T

def nearest_branch_ratio(omega0: float, Omega: float) -> int:
    """k = round(omega0/Omega)。どの折り返し枝か。"""
    return int(np.round(omega0 / Omega))

def apparent_omega(omega0: float, view: View) -> float:
    """ω_app = ω0 - kΩ。見かけ角速度（連続値）。"""
    k = nearest_branch_ratio(omega0, view.Omega)
    return omega0 - k * view.Omega

def jittered_period(T0: float, eta: np.ndarray) -> np.ndarray:
    """T(t) = T0 (1 + eta(t))。etaは小さなゆらぎ列。"""
    return T0 * (1.0 + eta)

def coincedent_frames_times(TL: float, TD: float, t_end: float, atol=1e-9) -> np.ndarray:
    """n TL = m TD の同時フレーム時刻を列挙（有限範囲）。"""
    # LCM風にやる：粗い格子で探索（実用的）
    tL = dirac_comb_times(TL, 0, t_end)
    tD = dirac_comb_times(TD, 0, t_end)
    hits = []
    j = 0
    for t in tL:
        while j < len(tD) and tD[j] < t - atol:
            j += 1
        if j < len(tD) and abs(tD[j] - t) <= atol:
            hits.append(t)
    return np.array(hits)
