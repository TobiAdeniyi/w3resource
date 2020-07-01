"9. Write a Python program to calculate the discriminant value."

# Note: The discriminant is the name given to the expression that
# appears under the square root (radical) sign in the quadratic formula.


import math

def discriminant():
    fun = input("Entter your function in the form - ax^2 + bx + c, where a, b and c are constants:")
    entries = fun.split(' + ')

    a = float(entries[0].split('x')[0])
    b = float(entries[1].split('x')[0])
    c = float(entries[2])

    disc = (b ** 2) - (4 * a * c)

    print(disc)
discriminant()
