"""31. Write a Python program to convert a decimal number to binary number."""


def to_binary(n):
    i = n
    sol = ""

    while i >1:
        # Concatenate 0 to sol if i is even, 1 if i is odd
        if i % 2 == 0:
            sol = "0" + sol
        else:
            sol = "1" + sol

        # Divide I by 2 and take the integer part
        i = int(i/2)

    # if n is zero
    if n == 0:
        sol = 0
    else:
        sol = "1" + sol

    print(f"Binary representation of {n}:", sol)

to_binary(0)
to_binary(13)
to_binary(43)
