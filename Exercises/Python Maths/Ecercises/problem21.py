""""21. Write a Python program to print all primes (Sieve_of_Eratosthenes)
smaller than or equal to a specified number."""

# In mathematics, the sieve of Eratosthenes, one of a number of prime number sieves, is a simple,
# ancient algorithm for finding all prime numbers up to any given limit.
# It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime,
# starting with the multiples of 2.


def primes(x):
    # check entry is not string
    if type(x) == str:
        x = input(print("This is not a number \nPleas enter a number:"))
        primes(x)

    # Entry should be  greater than 1 to get any result
    if x < 1:
        print(f"There are no prime numbers less than {x}")

    else:
        x = int(x)

        # Create saturated list to x
        N = [n for n in range(1, x)]
        notPrimes = set()

        # for each number up to x check if prime
        for n in N:
            for m in range(2, n):
                if n % m == 0:
                    notPrimes.add(n)
        list(notPrimes)
        for n in notPrimes:
            N.remove(n)

        print(N)

primes(100)

