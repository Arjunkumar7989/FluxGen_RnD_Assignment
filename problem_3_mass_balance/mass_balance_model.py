def mass_balance_components(rain, storage, outlet, infiltration, evaporation):
    """
    Mass balance with loss categorization
    """
    residual = rain - (storage + outlet + infiltration + evaporation)
    return {
        "Storage": storage,
        "Natural Loss": infiltration + evaporation,
        "Sensor/Error": residual
    }
