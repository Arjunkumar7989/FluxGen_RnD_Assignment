import numpy as np
from scipy.spatial.distance import cdist

def idw_interpolation(xy_known, z_known, xy_unknown, power=2):
    """
    Inverse Distance Weighting for spatial interpolation
    """
    dist = cdist(xy_unknown, xy_known)
    dist[dist == 0] = 1e-6
    weights = 1 / (dist ** power)
    weights /= weights.sum(axis=1, keepdims=True)
    return np.dot(weights, z_known)
