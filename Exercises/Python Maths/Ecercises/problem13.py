"13. Write a Python program to find out, if the given number is abundant."

# Note: In number theory, an abundant number or excessive number is
# a number for which the sum of its proper divisors is greater than the number itself.
# The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.


def is_abundant(n):
    k = 0

    for i in range(1, n):
        if n % i == 0:
            k += i

    if n >= k:
        print("False")
        print(f"{n} is not a abundant number.")
    else:
        print("True")
        print(f"{n} is an abundant number.")

is_abundant(100)

