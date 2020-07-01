"2. Write a Python program to convert radian to degree."


import math

x = input("Enter angle in Radians:")

x = float(x)

d = (x * 180) / math.pi

print(f"{x} Radians = {d} Degrees")
