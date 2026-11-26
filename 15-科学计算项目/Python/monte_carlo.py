"""用独立均匀抽样估计单位圆面积，并估计统计标准误。"""

import numpy as np


def estimate(samples=200_000, seed=2022):
    rng = np.random.default_rng(seed)
    points = rng.random((samples, 2))
    inside = np.sum(points**2, axis=1) <= 1
    fraction = np.mean(inside)
    standard_error = 4 * np.sqrt(fraction * (1 - fraction) / samples)
    return 4 * fraction, standard_error


def verify():
    value, standard_error = estimate()
    standardized_error = abs(value - np.pi) / standard_error
    assert 0 < value < 4
    assert standardized_error < 4
    return f"π估计={value:.5f}，统计标准误={standard_error:.5f}，绝对偏差={standardized_error:.2f} 个标准误"


if __name__ == "__main__":
    print(verify())
