"""有限缝宽双缝的夫琅禾费衍射。"""

import numpy as np


def intensity(angle, wavelength=550e-9, slit_width=20e-6, separation=80e-6):
    """角度采用弧度，三项长度采用米，返回相对轴上光强。"""
    direction = np.sin(angle) / wavelength
    envelope = np.sinc(slit_width * direction) ** 2
    interference = np.cos(np.pi * separation * direction) ** 2
    return envelope * interference


def verify():
    wavelength, width, separation = 550e-9, 20e-6, 80e-6
    angles = np.linspace(-0.07, 0.07, 501)
    symmetry_error = np.max(np.abs(intensity(angles) - intensity(-angles)))
    envelope_null = intensity(np.arcsin(wavelength / width))
    interference_null = intensity(np.arcsin(wavelength / (2 * separation)))
    assert intensity(0) == 1
    assert symmetry_error < 1e-13
    assert max(envelope_null, interference_null) < 1e-25
    return f"对称误差={symmetry_error:.3e}，包络及干涉首暗纹光强={envelope_null:.3e}、{interference_null:.3e}"


if __name__ == "__main__":
    print(verify())
