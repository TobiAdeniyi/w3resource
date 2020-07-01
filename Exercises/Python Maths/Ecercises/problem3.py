"Write a Python program to calculate the area of a trapezoid."

# Note : A trapezoid is a quadrilateral with two sides parallel.
# The trapezoid is equivalent to the British definition of the trapezium.
# An isosceles trapezoid is a trapezoid in which the base angles are equal so.


l1 = float(input("Enter its bottom length:"))

l2 = float(input("Enter its top length:"))

h = float(input("Enter its hight:"))

area = ((l1 + l2) / 2) * h

print(f"The area of your trapezoid is {area} squared units")
