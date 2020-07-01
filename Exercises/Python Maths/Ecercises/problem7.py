"Write a Python program to calculate arc length of an angle."

# Note: In a planar geometry, an angle is the figure formed by two rays,
# called the sides of the angle, sharing a common endpoint, called the vertex of the angle.
# Angles formed by two rays lie in a plane, but this plane does not have to be a Euclidean plane.


import math


pi = math.pi

def arclength():
    agl = float(input("Enter angle in Radians:"))
    r = float(input("Enter length:"))

    if agl > (2 * pi):
        agl = agl % (2 * pi)

    s = r * agl

    print(f"Arc length = {s} unit length")

arclength()
