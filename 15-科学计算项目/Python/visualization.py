"""绘制静电势、电场方向及谐振子能量。"""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from electrostatics import solve
from mechanics import simulate


def render(output):
    x, y, potential, field_x, field_y = solve(32)
    field_magnitude = np.hypot(field_x, field_y)
    nonzero = field_magnitude > 1e-12
    direction_x = np.divide(field_x, field_magnitude, out=np.zeros_like(field_x), where=nonzero)
    direction_y = np.divide(field_y, field_magnitude, out=np.zeros_like(field_y), where=nonzero)
    sample = np.s_[::4, ::4]
    time, position, velocity, _ = simulate(periods=2)

    figure, (field_axis, energy_axis) = plt.subplots(1, 2, figsize=(9, 4), layout="constrained")
    contours = field_axis.contourf(x, y, potential, levels=16, cmap="cividis")
    field_axis.quiver(
        x[sample], y[sample], direction_x[sample], direction_y[sample],
        color="white", angles="xy", scale_units="xy", scale=17,
    )
    field_axis.set(xlabel="x", ylabel="y", title="Potential and field direction", aspect="equal")
    figure.colorbar(contours, ax=field_axis, label="Potential (scaled)")

    energy_axis.plot(time, 0.5 * velocity**2, label="Kinetic", color="#147d73")
    energy_axis.plot(time, 0.5 * position**2, label="Potential", color="#b64b12")
    energy_axis.set(xlabel="Time (scaled)", ylabel="Energy (scaled)", title="Harmonic oscillator")
    energy_axis.legend(loc="upper right")
    figure.savefig(output, dpi=150)
    plt.close(figure)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="要写入的 PNG 路径")
    output = parser.parse_args().output
    if output.suffix.lower() != ".png":
        parser.error("输出路径必须以 .png 结尾")
    render(output)
    with output.open("rb") as file:
        assert file.read(8) == b"\x89PNG\r\n\x1a\n"
    print(f"PNG 文件已生成，{output.stat().st_size} 字节")


if __name__ == "__main__":
    main()
