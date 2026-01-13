import numpy as np

def delayed_outflow(input_signal, delay_hours):
    """
    Time-delay routing model
    """
    output = np.zeros_like(input_signal)
    output[delay_hours:] = input_signal[:-delay_hours]
    return output
