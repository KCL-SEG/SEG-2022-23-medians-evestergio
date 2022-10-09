"""Median calculator."""

def list_median(numbers):
    numbers.sort()
    mid = len(numbers)//2
    if len(numbers) % 2 != 0:
        return numbers[mid]
    else:
        return (numbers[mid] + numbers[mid-1]) / 2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(list_median(numbers))
