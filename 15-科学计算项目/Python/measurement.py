"""用方差已知的合成摆长与周期平方数据练习测量不确定度传播。"""

import numpy as np


def fit(length, period_squared, standard_uncertainty):
    """拟合 T²=a+bL，返回 g 及其标准不确定度和约化 χ²。"""
    design = np.column_stack((np.ones(length.size), length)) / standard_uncertainty[:, None]
    observations = period_squared / standard_uncertainty
    coefficients, *_ = np.linalg.lstsq(design, observations, rcond=None)
    slope = coefficients[1]
    covariance = np.linalg.inv(design.T @ design)
    g = 4 * np.pi**2 / slope
    g_uncertainty = abs(g / slope) * np.sqrt(covariance[1, 1])
    weighted_residuals = observations - design @ coefficients
    reduced_chi_squared = (weighted_residuals @ weighted_residuals) / (length.size - 2)
    return g, g_uncertainty, reduced_chi_squared


def verify():
    rng = np.random.default_rng(4)
    reference_g = 9.81
    length = np.linspace(0.30, 1.20, 20)
    uncertainty = np.linspace(0.012, 0.024, length.size)
    exact_period_squared = 4 * np.pi**2 * length / reference_g
    noiseless_g, _, noiseless_chi_squared = fit(length, exact_period_squared, uncertainty)
    period_squared = exact_period_squared + rng.normal(scale=uncertainty)
    g, g_uncertainty, reduced_chi_squared = fit(length, period_squared, uncertainty)
    assert abs(noiseless_g - reference_g) < 1e-12
    assert noiseless_chi_squared < 1e-20
    assert abs(g - reference_g) < 4 * g_uncertainty
    return f"合成数据拟合 g=({g:.4f} ± {g_uncertainty:.4f}) m/s²，约化 χ²={reduced_chi_squared:.3f}"


if __name__ == "__main__":
    print(verify())
