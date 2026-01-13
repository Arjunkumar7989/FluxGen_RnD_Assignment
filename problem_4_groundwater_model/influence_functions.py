def radial_influence(distance, strength, decay=2):
    """
    Radial decay influence
    """
    return strength / (distance**decay + 1e-6)
