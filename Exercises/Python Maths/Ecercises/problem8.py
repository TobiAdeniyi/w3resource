"8. Write a Python program to calculate the area of the sector."

# Note: A circular sector or circle sector, is the portion of a disk enclosed by two radii and an arc,
# where the smaller area is known as the minor sector and the larger being the major sector.


import math

pi = math.pi

def area_of_sector():
    r = float(input("Enter radius of sector:"))
    
    agl = float(input("Enter angle of sector in radians: "))
    
    if agl > (2 * pi):
        agl = agl % (2 * pi)

    area = 0.5 * agl * (r ** 2)

    print(f"The area of the sector = {area}")


area_of_sector()
