"""23. Write a python program to find the next previous palindrome of a specified number."""


def previous_largest_pal(x):
    # Iterate until we find a pal
    while True:
        # Change x back to integer
        x = int(x)

        # First value is  greater than x + 1 is a pal
        x = str(int(x) - 1)
        backwards_x = x[::-1]

        # if x looks the same forward and backwards
        if backwards_x == x:
            print(f"The next palindrome is {x}")
            return False



previous_largest_pal(input("Enter value:"))
