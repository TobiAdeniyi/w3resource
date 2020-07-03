"""27. Write a Python program to calculate the distance between two points using latitude and longitude."""

from geopy.distance import geodesic


def distance():
    start_long = input(print("Start longitude:"))
    start_lat = input(print("Start latitude:"))
    start = (float(start_long), float(start_lat))
    print("Your starting location is:", start)

    end_long = input(print("End longitude:"))
    end_lat = input(print("End latidude:"))
    end = (float(end_long), float(end_lat))
    print("Your ending location is:", end)

    print(geodesic(start, end).km)

distance()
