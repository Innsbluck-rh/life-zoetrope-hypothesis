# model/events.py
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class AuditClock:
    T_L: float  # audit period

def audit_ticks(clock: AuditClock, t_start: float, t_end: float) -> np.ndarray:
    return np.arange(np.ceil(t_start/clock.T_L), np.floor(t_end/clock.T_L)+1) * clock.T_L
