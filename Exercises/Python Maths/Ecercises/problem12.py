"12. Write a Python program to calculate the sum of all digits of the base to the specified power."



def power_bass_sum(x, y):
    n = sum([int(i) for i in str(pow(x, y))])
    print(n)

power_bass_sum(int(input("Enter base:")), int(input("Enter power:")))


