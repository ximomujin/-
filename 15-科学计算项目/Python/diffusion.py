"""以显式有限差分计算一维热方程。"""

from math import ceil

import numpy as np


def solve(intervals, time=0.2, diffusivity=0.3):
    """单位长度细杆，初温为 sin(πx)，两端恒为零。"""
    x = np.linspace(0.0, 1.0, intervals + 1)
    dx = 1 / intervals
    steps = max(1, ceil(time * diffusivity / (0.4 * dx**2)))
    ratio = diffusivity * (time / steps) / dx**2
    temperature = np.sin(np.pi * x)
    temperature[[0, -1]] = 0.0
    for _ in range(steps):
        temperature[1:-1] += ratio * (
            temperature[:-2] - 2 * temperature[1:-1] + temperature[2:]
        )
    expected = np.exp(-diffusivity * np.pi**2 * time) * np.sin(np.pi * x)
    return x, temperature, expected, ratio


def verify():
    _, coarse, coarse_exact, _ = solve(20)
    _, fine, fine_exact, ratio = solve(40)
    error = np.max(np.abs(fine - fine_exact))
    reduction = np.max(np.abs(coarse - coarse_exact)) / error
    assert ratio <= 0.5
    assert fine[0] == fine[-1] == 0
    assert 3.6 < reduction < 4.4
    return f"40 等分温度误差={error:.3e}，加密前后误差之比={reduction:.2f}，r={ratio:.3f}"


if __name__ == "__main__":
    print(verify())
