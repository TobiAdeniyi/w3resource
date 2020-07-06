"""30. Write a Python program to find the roots of a quadratic function."""


import math

def quad_func(a = 0, b = 0, c = 0):
    print(f"Quadratic function: a(x^2) + bx + c")
    print("a:", a)
    print("b:", b)
    print("c:", c)

    # Quadratic equation with no real solution
    if ((b ** 2) - 4 * a * c) < 0:
        print("There are no real roots")

    # Linear Equation with single root
    elif a == 0 and b != 0:
        r = (-c) / b
        print(f"There is one root: {r}")

    # Linear Equation with no root
    elif a == 0 and b == 0:
        if c == 0:
            print("The whole real line \'R\' is a solution")
        else:
            print("There are no solutions")

    # Quadratic Equation with solution
    else:
        r1 = (-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

        # Single root
        if r1 == r2:
            print(f"There is a single root: {r1}")

        # Double root
        else:
            print(f"There are 2 roots: {r1} and {r2}")


quad_func(25, 64, 36)
quad_func()
