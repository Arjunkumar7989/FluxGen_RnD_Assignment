import numpy as np
from influence_functions import radial_influence

def compute_drawdown(grid_shape, location, strength):
    """
    Computes drawdown field for ONE source
    """
    n = grid_shape[0]
    drawdown = np.zeros(grid_shape)
    sx, sy = location

    for i in range(n):
        for j in range(n):
            d = ((i - sx)**2 + (j - sy)**2) ** 0.5
            drawdown[i, j] = radial_influence(d, strength)

    return drawdown


def apply_multiple_sources(base_grid, sources, min_head=0):
    """
    Applies all sources via superposition (physically correct)
    """
    total_drawdown = np.zeros_like(base_grid)

    for src in sources:
        dd = compute_drawdown(
            base_grid.shape,
            src["location"],
            src["strength"]
        )
        total_drawdown += dd

    updated_grid = base_grid - total_drawdown
    updated_grid = np.clip(updated_grid, min_head, None)

    return updated_grid
