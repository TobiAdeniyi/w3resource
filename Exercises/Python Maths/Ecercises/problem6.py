"6. Write a Python program to calculate surface volume and area of a sphere."

# Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball.


import math

r = float(input("Enter the radius of the sphere:"))

Area = 4 * math.pi * (r ** 2)

Volume = (4 / 3) * math.pi * (r ** 3)

print(f"Surface area = {Area}, Volume = {Volume}")
