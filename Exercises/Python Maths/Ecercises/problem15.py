"""15. Write a Python program to returns sum of all divisors of a number."""



def sum_divisors(n):
    if not isinstance(n, int) or n < 1:
        if n == "exit":
            print("Exited")
            # Need to add a line of code to exit the sum_divisors function
        print("Please input positive integer or type exit to quit.")
        n = int(input("Enter new input:"))
        sum_divisors(n)
    else:
        k = 0
        for i in range(1, n):
            if n % i == 0:
                print(i)
                k += i

    print(f"The sum of the divisors of {n} is  {k}")

sum_divisors(8)

