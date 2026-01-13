import numpy as np

def monte_carlo(depth, std_dev, n=2000):
    """
    Monte Carlo uncertainty propagation
    """
    samples = np.random.normal(depth, std_dev, (n, len(depth)))
    return samples.mean(axis=1)
