"1. Write a Python program to convert degree to radian."

# Note: The radian is the standard unit of angular measure, used in many areas of mathematics.
# An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle;
# one radian is just under 57.3 degrees (when the arc length is equal to the radius)."


import math

x = input("Enter angel in Degrees:")

x = float(x)

r = (x * math.pi) / 180

print(f'{x} Degrees = {r} Radians')


