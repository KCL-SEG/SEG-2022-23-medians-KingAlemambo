"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        numbers.sort()
        n=len(numbers)//2
        median =0
        if len(numbers) % 2 == 0:
            median=(numbers[n] + numbers[n+1])//2
        else:
            median=numbers[n]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)



