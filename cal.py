#!/usr/bin/env python3
def calculate_average():
    """
    Calculates the average of a list of numbers entered by the user.

    Returns:
        float: The average of the numbers.
    """
    numbers = input("Enter a list of numbers, separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count == 0:
        return 0
    else:
        return total / count

average = calculate_average()
print(average)

