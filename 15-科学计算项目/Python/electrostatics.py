"""在单位正方形内求解二维静电势及电场。"""

import numpy as np
from scipy.sparse import diags, kronsum
from scipy.sparse.linalg import spsolve


def solve(intervals):
    """采用五点差分。上边界为 sin(πx)，其余三个边界为零。"""
    axis = np.linspace(0, 1, intervals + 1)
    potential = np.zeros((axis.size, axis.size))
    potential[-1, 1:-1] = np.sin(np.pi * axis[1:-1])
    rhs = np.zeros_like(potential[1:-1, 1:-1])
    rhs[-1] = potential[-1, 1:-1]
    # 系数矩阵及右端同时乘以网格步长平方。
    one_dimensional = diags((-1.0, 2.0, -1.0), (-1, 0, 1), shape=rhs.shape, format="csr")
    operator = kronsum(one_dimensional, one_dimensional, format="csr")
    potential[1:-1, 1:-1] = spsolve(operator, rhs.ravel()).reshape(rhs.shape)
    x, y = np.meshgrid(axis, axis)
    dy, dx = np.gradient(potential, axis, axis, edge_order=2)
    return x, y, potential, -dx, -dy


def analytical(x, y):
    potential = np.sin(np.pi * x) * np.sinh(np.pi * y) / np.sinh(np.pi)
    field_x = -np.pi * np.cos(np.pi * x) * np.sinh(np.pi * y) / np.sinh(np.pi)
    field_y = -np.pi * np.sin(np.pi * x) * np.cosh(np.pi * y) / np.sinh(np.pi)
    return potential, field_x, field_y


def error(intervals):
    x, y, *computed = solve(intervals)
    return [
        np.max(np.abs(actual - expected))
        for actual, expected in zip(computed, analytical(x, y))
    ]


def verify():
    coarse_potential_error, _, _ = error(16)
    potential_error, field_x_error, field_y_error = error(32)
    reduction = coarse_potential_error / potential_error
    assert 3.8 < reduction < 4.2
    assert max(field_x_error, field_y_error) < 0.013
    return (
        f"32 等分势误差={potential_error:.3e}，"
        f"电场分量峰值误差={max(field_x_error, field_y_error):.3e}，"
        f"加密前后势误差之比={reduction:.2f}"
    )


if __name__ == "__main__":
    print(verify())
