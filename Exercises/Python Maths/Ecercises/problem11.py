"""11. Write a Python program to calculate the difference between the squared sum of first n natural numbers
and the sum of squared first n natural numbers.(default value of number=2)."""


def sum_calculator():
    n = int(input("Enter (integer) value of n:"))

    if True:
        if n < 0:
            print("Erro! n must be positive")
        elif n < 2 and n >= 0:
            print(f"Mean square difference is {0}")
        else:
            N = 0

            M = 0

            for i in range(n):
                N = N + (i ** 2)
                M = M + i

            M = M ** 2

            print("Mean squared difference is:", M - N)

    else:
        print("For 2 the MSD is:", 5)

sum_calculator()
