import numpy as np

def cumulative_stress(grid):
    """
    Stress = magnitude of head gradient
    """
    gx, gy = np.gradient(grid)
    return (gx**2 + gy**2) ** 0.5
