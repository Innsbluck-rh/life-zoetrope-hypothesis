# model/world.py
from dataclasses import dataclass
import numpy as np

@dataclass(frozen=True)
class World:
    omega0: float  # true angular speed [rad/s]

    def phasor(self, t: np.ndarray) -> np.ndarray:
        """angle(t) = omega0 * t (mod 2π) を返す（可視化用に実角もOK）。"""
        return (self.omega0 * t) % (2*np.pi)
