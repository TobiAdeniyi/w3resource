"10. Write a Python program to find the smallest multiple of the first n numbers. Also, display the factors."


m = int(input("What number would yo like to know the smallest common multiple for?"))

def smallest_multiple(n):
    print("The list of factors of factors is:")

    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    print(f"The smallest common multiple for all values less than  or equal to {n}, is:")

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i


print(smallest_multiple(m))
