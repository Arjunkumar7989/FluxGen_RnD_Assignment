import numpy as np

def volume_monte_carlo(depth_grid, cell_area, depth_std, n=2000):
    """
    Volume estimation with uncertainty
    """
    volumes = []
    for _ in range(n):
        noisy_depth = depth_grid + np.random.normal(0, depth_std, depth_grid.shape)
        noisy_depth = np.clip(noisy_depth, 0, None)
        volumes.append(np.sum(noisy_depth * cell_area))
    return np.mean(volumes), np.std(volumes)
