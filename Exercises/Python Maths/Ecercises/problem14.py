"14. Write a Python program to sum all amicable numbers from 1 to specified numbers."

# Note: Amicable numbers are two different numbers so related that the sum
# of the proper divisors of each is equal to the other number.
# (A proper divisor of a number is a positive factor of that number other than the number itself.
# For example, the proper divisors of 6 are 1, 2, and 3.)


"""

def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"

    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit+1):
        if num in amicables:
            continue

        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return sum(amicables)


print(amicable_numbers_sum(9999))
print(amicable_numbers_sum(999))
print(amicable_numbers_sum(99))


"""


x = int(input("Enter number:"))
#N = list(int(range(n)))


k = 0
l = 0
i = 1

def Proper_divisors(n):
    A = []
    for i in range(2, n):
        if n % i == 0:
            A.append(i)
    return A
    #print(f"{n} has proper divisors{A}")


while i < x:
    print(i)
    j = i + 1
    while j <= x:
        print(j)
        print(Proper_divisors(i), Proper_divisors(j))
        if Proper_divisors(i) == Proper_divisors(j) and Proper_divisors(i) != []:
            k += 1
            l = j
        j += 1
    print(f"Total count is now {k}, the last number was {l}")
    i += 1

k = k + l
print(k)
