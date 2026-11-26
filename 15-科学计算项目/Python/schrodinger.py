"""一维无限深势阱的定态薛定谔方程。"""

import numpy as np
from scipy.linalg import eigh_tridiagonal


def solve(intervals=160, state_count=4):
    """在 x/L 网格上返回能量 2mL²E/ℏ² 和无量纲归一化波函数。"""
    x = np.linspace(0, 1, intervals + 1)
    diagonal = np.full(intervals - 1, 2 * intervals**2, dtype=float)
    off_diagonal = np.full(intervals - 2, -intervals**2, dtype=float)
    energies, vectors = eigh_tridiagonal(
        diagonal, off_diagonal, select="i", select_range=(0, state_count - 1)
    )
    wavefunctions = np.zeros((x.size, state_count))
    wavefunctions[1:-1] = np.sqrt(intervals) * vectors
    return x, energies, wavefunctions


def verify():
    x, energies, states = solve()
    exact = (np.pi * np.arange(1, energies.size + 1)) ** 2
    energy_error = np.max(np.abs(energies / exact - 1))
    overlap = (states.T @ states) * (x[1] - x[0])
    overlap_error = np.max(np.abs(overlap - np.eye(energies.size)))
    assert energy_error < 6e-4
    assert overlap_error < 1e-12
    assert np.all(states[[0, -1]] == 0)
    return f"前四个能级最大相对误差={energy_error:.3e}，正交归一误差={overlap_error:.3e}"


if __name__ == "__main__":
    print(verify())
