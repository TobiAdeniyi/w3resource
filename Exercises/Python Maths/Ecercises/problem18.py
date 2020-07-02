"""18. Write a Python program to computing square roots using the Babylonian method."""

# Perhaps the first algorithm used for approximating √S is known as the Babylonian method,
# named after the Babylonians, or "Hero's method", named after the first-century Greek
# mathematician Hero of Alexandria who gave the first explicit description of the method.
# It can be derived from (but predates by 16 centuries) Newton's method.
# The basic idea is that if x is an overestimate to the square root of a non-negative real
# number S then S / x will be an underestimate and so the average of these two numbers may
# reasonably be expected to provide a better approximation.



def square_root(y):
    if y < 0:
        print("Entry must be non-negative")
    elif y == 0:
        print(0)
    else:
        x = y + 2
        while x**2 - y > 10e-10:
            x = ((x + y / x) / 2)
        else:
            print(f"The square root of {y} is {x} to 11 dp")

square_root(1234567890)
