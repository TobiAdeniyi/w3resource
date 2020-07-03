"""28. Write a Python program to calculate the area of regular polygon."""


import math

def area_orRegPol(n, x):
    A = (n * (x ** 2)) / (4 * math.tan((math.pi) / n))
    print(A)

area_orRegPol(4, 25)
