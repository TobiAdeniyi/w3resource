"""32. Write a Python program to print a complex number and its real and imaginary parts."""


def complex(comp_num):
    #vector_form = (str(comp_num)[1:-1]).split("+")
    #print(f"Complex Number: {comp_num} \nComplex Number - Real part: {float(vector_form[0])} \nComplex Number - Imaginary part: {float(vector_form[1][:-1])}")
    print(f"Complex Number: {comp_num} \nComplex Number - Real part: {comp_num.real} \nComplex Number - Imaginary part: {comp_num.imag}")

complex(2+2j)


