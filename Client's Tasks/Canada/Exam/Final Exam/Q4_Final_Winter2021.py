import numpy as np

def ellipse(a, b, intervals):
    x = np.linspace(-a, a, intervals + 1)   # creating equally spaced x coordinates value ranging -a to a
    y = b * np.sqrt(1 - (x / a) ** 2)   # creating corresponding y coordinates values based on equation 1

    return x, y     # return the array of x,y coordinate of ellipse



