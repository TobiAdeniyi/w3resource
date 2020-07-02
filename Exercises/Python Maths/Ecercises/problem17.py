"""16. Write a Python program to print the first n Lucky Numbers."""

# Lucky numbers are defined via a sieve as follows.
# Begin with a list of integers starting with 1 :
# 1, 2, 3,	4, 5, 6,	7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, . . . .
# Now eliminate every second number :
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, ...
# The second remaining number is 3, so remove every 3rd number:
# 1, 3, 7, 9, 13, 15, 19, 21, 25, ...
# The next remaining number is 7, so remove every 7th number:
# 1, 3, 7, 9, 13, 15, 21, 25, ...
# Next, remove every 9th number and so on.
# Finally, the resulting sequence is the lucky numbers.




def magic(n):
    # Create list Element "Initial list"
    lst = []
    for i in range(1, n + 1):
        lst.append(i)
    print(f"Our initial list is {lst}")
    print(" ")

    # Create Ordinal function
    ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
    x = 2
    y = 1

    # Inform user of what step they are in
    print(f"1) X = {x}, Y = {y}")
    print(f"Remove every {ordinal(x)} number from our list gives:")

    # Iterate until the end of list
    while x < len(lst):

        # Initialise "Remove list" as empty list
        rmv_lst = []

        # For each element in a position divisible by x
        for i in range(1, len(lst) + 1):
            if i in lst and (lst.index(i) + 1) % x == 0:
                # Add elements to "Remove list"
                rmv_lst.append(i)

        print(f"list of numbers to remove: {rmv_lst}")

        # for each element in the "Remove list"
        for elements in rmv_lst:
            # if the element is still in our "Initial list"
            if elements in lst:
                # remove the element
                lst.remove(elements)

        print(f"Leaving list = {lst}")
        print(" ")

        # Update variables
        x = lst[y]
        y += 1
        print(f"{y}) X = {x}, Y = {y}")
        print(f"Remove every {ordinal(x)} number from our list")


magic(100)

