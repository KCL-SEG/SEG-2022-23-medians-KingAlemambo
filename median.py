"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

def findMedian(numbers):
    print("enter median method   ")
    numbers.sort()
    n=numbers.length()/2
    if numbers.length() % 2 == 0:
        median=(numbers[n] + numbers[n+1])/2
    else:
        median=numbers[n]
    print("median method finished")
    return median

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        findMedian(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)