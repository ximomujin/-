"""二原子链振动及单轨道近邻紧束缚能带。"""

import numpy as np


def phonons(phase, mass_1=1.0, mass_2=2.0, spring=1.0):
    """phase=ka，返回二原子链的声学和光学支角频率。"""
    inverse_mass_sum = 1 / mass_1 + 1 / mass_2
    splitting = np.sqrt(
        (1 / mass_1 - 1 / mass_2) ** 2
        + 4 * np.cos(phase / 2) ** 2 / (mass_1 * mass_2)
    )
    acoustic = np.sqrt(spring * np.maximum(0, inverse_mass_sum - splitting))
    optical = np.sqrt(spring * (inverse_mass_sum + splitting))
    return acoustic, optical


def electron_band(phase, on_site_energy=0, hopping=1):
    """在单独的一维单轨道模型中计算电子能量。"""
    return on_site_energy - 2 * hopping * np.cos(phase)


def verify():
    phases = np.linspace(-np.pi, np.pi, 401)
    acoustic, optical = phonons(phases)
    acoustic_center, optical_center = phonons(0.0)
    edge = phonons(np.pi)
    branch_error = np.max(np.abs(np.array([acoustic_center, optical_center, *edge]) - [
        0, np.sqrt(3), 1, np.sqrt(2)
    ]))
    energies = electron_band(phases)
    bandwidth = np.ptp(energies)
    assert branch_error < 1e-13
    assert np.all(acoustic <= optical)
    assert abs(bandwidth - 4) < 1e-13
    return f"晶格振动分支端点偏差={branch_error:.3e}，紧束缚带宽={bandwidth:.3f}（跃迁能为 1）"


if __name__ == "__main__":
    print(verify())
