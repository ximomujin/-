"""傍轴自由传播和薄透镜折射。"""

import numpy as np


def trace(height, slope, object_distance, focal_length, image_distance):
    """返回透镜后的像面光线高度，距离单位为米。"""
    lens_height = height + object_distance * slope
    exit_slope = slope - lens_height / focal_length
    return lens_height + image_distance * exit_slope


def verify():
    focal_length, object_distance, object_height = 0.10, 0.15, 0.01
    image_distance = 1 / (1 / focal_length - 1 / object_distance)
    magnification = -image_distance / object_distance
    slopes = np.linspace(-0.10, 0.05, 11)
    image_heights = trace(object_height, slopes, object_distance, focal_length, image_distance)
    image_error = np.max(np.abs(image_heights - magnification * object_height))
    parallel_heights = np.linspace(-0.02, 0.02, 11)
    focus_error = np.max(np.abs(trace(parallel_heights, 0, 0, focal_length, focal_length)))
    assert image_error < 1e-14
    assert focus_error < 1e-14
    return (
        f"像距={image_distance:.3f} m，横向放大率={magnification:.2f}，"
        f"像面及平行光聚焦偏差={image_error:.3e} m、{focus_error:.3e} m"
    )


if __name__ == "__main__":
    print(verify())
