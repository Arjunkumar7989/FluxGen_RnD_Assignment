def temperature_corrected_mass(volume, delta_temp):
    """
    Prevents thermal expansion misinterpretation
    """
    beta = 0.00021
    return volume / (1 + beta * delta_temp)
