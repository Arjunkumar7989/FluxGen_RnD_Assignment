import numpy as np

def initialize_grid(n, initial_head=100):
    """
    Groundwater head grid
    """
    return np.full((n, n), initial_head, dtype=float)
