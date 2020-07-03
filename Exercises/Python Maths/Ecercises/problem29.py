"""29. Write a Python program to calculate wind chill index."""


import math

def WCI(v, t):
    # v = wind speed, t = air temperature
    chill = (10 * math.sqrt(v * 1000 / 3600) - (v * 1000 / 3600) + 10.5) * (33 - t)
    print(chill)

WCI(150, 29)
