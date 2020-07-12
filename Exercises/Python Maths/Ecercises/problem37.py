"""37. Write a Python program to find sum of the following decimal numbers and display the numbers in sorted order."""


def fun37(lst):
    state = all(isinstance(n, float) for n in lst)
    if state:
        N = sum(lst)
        lst = sorted(lst)
        print(f"Sum list: {N} \nOrdered list: {lst}")
    else:
        print("This list contains none numerical elements \nPlease input numerical list")


newLst = list(float(i) for i in input("Please Enter list of numbers")[1:-1].split(", "))
fun37(newLst)
