import numpy as np

def spatial_weighted_risk(sat_score, ground_truth, distance_km):
    """
    Distance-based confidence weighting
    """
    weight = np.exp(-distance_km / 5)
    return (sat_score * weight + ground_truth * (1 - weight))
