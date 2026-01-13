def spectral_consistency(green, nir):
    """
    Detects optical false positives using NIR
    """
    ratio = green / (nir + 1e-6)
    if ratio > 1.2:
        return "Optical Error Likely"
    return "Biological Signal Possible"
