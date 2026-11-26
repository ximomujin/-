"""无阻尼谐振子，采用速度 Verlet 积分。"""

import numpy as np


def simulate(dt=0.02, periods=8):
    """返回时间、位移、速度和能量。采用 m=k=1、x(0)=1、v(0)=0。"""
    steps = round(periods * 2 * np.pi / dt)
    time = dt * np.arange(steps + 1)
    position = np.empty_like(time)
    velocity = np.empty_like(time)
    position[0], velocity[0] = 1.0, 0.0
    for step in range(steps):
        half_velocity = velocity[step] - 0.5 * dt * position[step]
        position[step + 1] = position[step] + dt * half_velocity
        velocity[step + 1] = half_velocity - 0.5 * dt * position[step + 1]
    energy = 0.5 * (position**2 + velocity**2)
    return time, position, velocity, energy


def verify():
    time, position, _, energy = simulate()
    displacement_error = np.max(np.abs(position - np.cos(time)))
    relative_energy_error = np.max(np.abs(energy / energy[0] - 1))
    assert displacement_error < 1e-3
    assert relative_energy_error < 1.01e-4
    return (
        f"最大位移误差={displacement_error:.3e}，"
        f"最大相对能量偏差={relative_energy_error:.3e}"
    )


if __name__ == "__main__":
    print(verify())
