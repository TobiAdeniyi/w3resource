"""Write a Python program to multiply two integers without using the * operator in python."""


def complex_multiplication(a, b):
    x= 0
    if a > 0:
        for i in range(a):
            x += b
    elif a < 0:
        for i in range(a, 0):
            x -= b
    print(x)

complex_multiplication(0, 0)
