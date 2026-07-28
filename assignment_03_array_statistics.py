# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def calculate_minimum(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


count = int(input("How many numbers? "))

if count <= 0:
    print("Error: Number of values must be greater than 0.")
else:
    values = []

    for i in range(count):
        value = float(input(f"Enter number {i + 1}: "))
        values.append(value)

    total = calculate_sum(values)
    average = calculate_average(values)
    maximum = calculate_maximum(values)
    minimum = calculate_minimum(values)

    print("\nResults:")
    print("Sum:    ", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
