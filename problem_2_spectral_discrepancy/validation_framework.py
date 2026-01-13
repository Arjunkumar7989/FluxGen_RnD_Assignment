def validation_framework(greenness, cloud, temperature, wind):
    """
    Validation firewall before alert
    """
    if cloud > 0.35:
        return "BLOCK: Cloud Contamination"
    if temperature < 18:
        return "BLOCK: Low Biological Activity"
    if wind > 12:
        return "BLOCK: Surface Reflection Risk"
    return "ALERT CONFIRMED"
