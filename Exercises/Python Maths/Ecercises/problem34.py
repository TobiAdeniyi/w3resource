"""34. Write a Python program to get the length and the angle of a complex number."""
import math
import cmath


def polar_form(complex):
    # re = complex.real
    # im = complex.imag

    # rad = math.sqrt(re**2 + im**2)
    # agl = math.tan(im / re)

    # print(rad)
    # print(agl)

    cmplx = cmath.polar(complex)
    print(f"Length of a complex number: {cmplx[0]}\nComplex number Angle: {cmplx[1]}")


polar_form(1+1j)
